#!coding: utf-8
from __future__ import print_function, division

from OpenGL.GL import *
from OpenGL.GL import shaders

from vec3_utils import farray
from vec3_utils import *
import pygame
pygame.init()


tick = 0
taille = [1280, 720]
ecran = pygame.display.set_mode(taille, pygame.OPENGL|pygame.DOUBLEBUF)


# with open('boomerang.obj') as f:
with open('boomerang.obj') as f:
    points = []
    vertices = []
    for line in f:
        d = line.split()
        if d[0] == 'v':
            points.append( [float(d[1]), float(d[2]), float(d[3])] )
        else:
            if d[0] == 'f':
                i1 = int(d[1].split('/')[0])
                i2 = int(d[2].split('/')[0])
                i3 = int(d[3].split('/')[0])
                vertices.extend( points[i1 - 1] )    
                vertices.extend( points[i2 - 1] )  
                vertices.extend( points[i3 - 1] )
    vertices = farray(vertices)

"""
vertices = farray([
    -0.5, 0.0, 0.4, 
    0.0, 0.5, 0.4,
    0.5, 0.0, 0.4, 
    
    -0.25, 0, 0.4, 
    0.0 , 0.0, 0.4, 
    -0.25, -0.6, 0.4, 
    
    -0.25, -0.6, 0.4, 
    0, 0.0, 0.4, 
    0.25, -0.6, 0.4, 
    
    0.25, 0, 0.4, 
    0.0, 0.0, 0.4, 
    0.25, -0.6, 0.4, 
    
    0.25, 0.8, 0.4, 
    0.10, 0, 0.8, 
    0.10, -0.6, 0.4,     
])
"""

import random

colors = []
for i in range(len(vertices)):
    x = random.uniform(0, 1)
    colors.append(x)

colors = farray(colors)


vertex_shader =''' 
#version 330
in vec3 position;
in vec3 color;

uniform mat4 thematrix;
out vec3 fcolor;

void main()
{
    gl_Position = thematrix * vec4(position, 1);
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
inconnuerotation = 0
sens = 1
t = 0
fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    
    t = -tick 
    translation = farray((0.5, 0.2, 0.1))
    if inconnuerotation == 300:
        sens =0
    if inconnuerotation == -300:
        sens =1
        sens = 0
    if sens == 1:
        inconnuerotation += 1
        tick +=1
    if sens == 0:
        inconnuerotation -=1
        tick -=1
    if t < 0:
        u = -t
    if t == 0:
        u=1
    if t >0:
        u = t
    # DESSIN
    glClearColor(0, 0.2, 0.4, 0.8) # jaune
    glClear(GL_COLOR_BUFFER_BIT) # fill  
    
    glUseProgram(shader_program)
    
    
    
    
    #translation = t*farray((0.010, 0.015, 0))
    #loc_translation = glGetUniformLocation(shader_program, 'translation')
    #glUniform3fv(loc_translation, 1, translation)
    
    P = PerspectiveMatrix(45*(1), 1.0 * 1280/720, 0.01, 10)
        
    # build view matrix (lookAt)
    V = LookAtMatrix((0.15)*vec3(2,0,1), (0, 0, 0), (0, 0, 1))    
    
    T = TranslationMatrix(farray((0.010, 0.015, 0.02)))
    S = ScaleMatrix(t*0.0055*0.08)
    R = RotationMatrix(20*t, (0,0,1))
    M = R @ T @ S
    glUniformMatrix4fv(glGetUniformLocation(shader_program, 'thematrix'), 1, True, P @ V @ M)
    
    #loc_grand = glGetUniformLocation(shader_program, 'grand')
    # glUniform1f(loc_grand, 0.7)
    
    glBindVertexArray(vertex_array_object)
    glDrawArrays(GL_TRIANGLES, 0, len(vertices) // 3) # on a 3 points, on commence au point numéro 0, faire des TRIANGLES.
    glBindVertexArray(0)
    
    glUseProgram(0)    
    # pygame.draw.rect(ecran, ROUGE, [100,200, 20,40])
    # pygame.draw.circle(ecran, BLEU, [100,200], 20)
    # pygame.draw.circle(ecran, VERT, [150, 80], 10)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
