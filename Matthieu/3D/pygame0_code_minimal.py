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
    -0.5, 0.0, 0.0, 1.0,
    0.0, 0.5, 0.0, 1.0,
    0.5, 0.0, 0.0, 1.0,
    
    -0.25, 0, 0.0, 1.0,
    0.0 , 0.0, 0.0, 1.0,
    -0.25, -0.6, 0.0, 1.0,
    
    -0.25, -0.6, 0.0, 1.0,
    0, 0.0, 0.0, 1.0,
    0.25, -0.6, 0.0, 1.0,
    
    0.25, 0, 0.0, 1.0,
    0.0, 0.0, 0.0, 1.0,
    0.25, -0.6, 0.0, 1.0,
])


vertex_shader =''' 
#version 330
in vec4 position;

void main()
{
    gl_Position = position; // et on l'écrit
}'''

fragment_shader = '''
#version 330
// fragment shader

out vec4 pixel; // notre but est de donner la couleur du pixel

void main() {
    pixel = vec4(1, 0.5, 0, 1); // orange, transparence 100%
}
'''

shader_program = shaders.compileProgram(
    shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
    shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))

vertex_buffer = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer) # manipulation glBindBuffer(GL_ARRAY_BUFFER, 0) 
glBufferData(GL_ARRAY_BUFFER, ArrayDatatype.arrayByteCount(vertices), vertices, GL_STATIC_DRAW) # 48 bytes
glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
glBufferData(GL_ARRAY_BUFFER, ArrayDatatype.arrayByteCount(vertices), vertices, GL_STATIC_DRAW)
vertex_array_object = glGenVertexArrays(1)
glBindVertexArray(vertex_array_object)

# manipulation
position = glGetAttribLocation(shader_program, 'position')
if position != -1:
    glEnableVertexAttribArray(position) # on active l'attribut 0
    glVertexAttribPointer(position, 4, GL_FLOAT, False, 0, ctypes.c_void_p(0)) # données par groupe de 4 Float dans l'attribut 0

glBindVertexArray(0)


NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

# DÉBUT

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    
    glClearColor(0.9, 0.9, 0.5, 1.0) # jaune
    glClear(GL_COLOR_BUFFER_BIT) # fill
    
    # DESSIN
    glUseProgram(shader_program)
    
    glBindVertexArray(vertex_array_object)
    glDrawArrays(GL_TRIANGLES, 0, 12) # on a 3 points, on commence au point numéro 0, faire des TRIANGLES.
    glBindVertexArray(0)
    
    glUseProgram(0)    
    # pygame.draw.rect(ecran, ROUGE, [100,200, 20,40])
    # pygame.draw.circle(ecran, BLEU, [100,200], 20)
    # pygame.draw.circle(ecran, VERT, [150, 80], 10)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
