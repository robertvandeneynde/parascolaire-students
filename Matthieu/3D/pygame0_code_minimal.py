#!coding: utf-8
from __future__ import print_function, division

from OpenGL.GL import *
from OpenGL.GL import shaders

from vec3_utils import farray
import pygame
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille, pygame.OPENGL|pygame.DOUBLEBUF)




vertices = farray([
    -0.5, 0.0, 0.5, 
    0.0, 0.5, 0.6, 
    0.5, 0.0, 0.4, 
    
    -0.25, 0, 0.0, 
    0.0 , 0.0, 0.0, 
    -0.25, -0.6, 0.0, 
    
    -0.25, -0.6, 0.0, 
    0, 0.0, 0.0, 
    0.25, -0.6, 0.0, 
    
    0.25, 0, 0.0, 
    0.0, 0.0, 0.0, 
    0.25, -0.6, 0.0, 
])

colors = farray([
    1,0,0,
    0,1,0,
    0,0,1,
    
    1,0,0,
    0,1,0,
    0,0,1,

    1,0,0,
    0,1,0,
    0,0,1,
    
    1,0,0,
    0,1,0,
    0,0,1,
])


vertex_shader =''' 
#version 330
in vec3 position;
in vec3 color;
uniform vec3 translation;
uniform float grand;
out vec3 fcolor;

void main()
{
    gl_Position = vec4(grand * position * translation, 1); // et on l'écrit
    fcolor = color;
}'''

fragment_shader = '''
#version 330
// fragment shader

in vec3 fcolor;
out vec4 pixel; // notre but est de donner la couleur du pixel

void main() {
    pixel = vec4(fcolor, 1); // vec4(1, 0.2, 0.4, 1); // orange, transparence 100%
}
'''

shader_program = shaders.compileProgram(
    shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
    shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))

vertex_array_object = glGenVertexArrays(1)
glBindVertexArray(vertex_array_object)

vertex_buffer = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer) # manipulation glBindBuffer(GL_ARRAY_BUFFER, 0) 
glBufferData(GL_ARRAY_BUFFER, ArrayDatatype.arrayByteCount(vertices), vertices, GL_STATIC_DRAW) # 48 bytes

# manipulation
position = glGetAttribLocation(shader_program, 'position')
if position != -1:
    glEnableVertexAttribArray(position) # on active l'attribut 0
    glVertexAttribPointer(position, 3, GL_FLOAT, False, 0, ctypes.c_void_p(0)) # données par groupe de 4 Float dans l'attribut 0

color_buffer = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, color_buffer)
glBufferData(GL_ARRAY_BUFFER, ArrayDatatype.arrayByteCount(colors), colors, GL_STATIC_DRAW)

color = glGetAttribLocation(shader_program, 'color')
if color != -1:
    glEnableVertexAttribArray(color) # on active l'attribut 1
    glVertexAttribPointer(color, 3, GL_FLOAT, False, 0, ctypes.c_void_p(0)) # données par groupe de 4 Float dans l'attribut 0

glBindVertexArray(0)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

# DÉBUT

clock = pygame.time.Clock()

t = 0
fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    translation = farray((0.5, 0.2, 0.1))
    
    # DESSIN
    glClearColor(0.6, 0.3, 0.4, 1.0) # jaune
    glClear(GL_COLOR_BUFFER_BIT) # fill  
    
    glUseProgram(shader_program)
    
    if t ==10:
        t -=1
    else:
        t +=1
    
    translation = t*farray((0.1, 0.2, 0))
    loc_translation = glGetUniformLocation(shader_program, 'translation')
    glUniform3fv(loc_translation, 1, translation)
    
    loc_grand = glGetUniformLocation(shader_program, 'grand')
    glUniform1f(loc_grand, 0.5*t)
    
    glBindVertexArray(vertex_array_object)
    glDrawArrays(GL_TRIANGLES, 0, 12) # on a 3 points, on commence au point numéro 0, faire des TRIANGLES.
    glBindVertexArray(0)
    
    glUseProgram(0)    
    # pygame.draw.rect(ecran, ROUGE, [100,200, 20,40])
    # pygame.draw.circle(ecran, BLEU, [100,200], 20)
    # pygame.draw.circle(ecran, VERT, [150, 80], 10)
    
    pygame.display.flip()
    
    clock.tick(10)
    
pygame.quit()
