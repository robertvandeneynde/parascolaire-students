#!coding: utf-8
from __future__ import print_function, division
from OpenGL.GL import *
from OpenGL.GL import shaders
from vec3_utils import *
# créer un compte sur github.com, fork gitub.com/robertvandeneynde/parascolaire-students, clone, modif, commit, push, pull request

import pygame
pygame.init()

pygame.display.set_mode((1280, 720), pygame.OPENGL | pygame.DOUBLEBUF)

NOIR = [0, 0, 0]
BLANC = [1, 1, 1]
ROUGE = [1, 0, 0]
VERT = [0, 1, 0]
BLEU = [0, 0, 1]

vertex_shader = '''
// contenu du vertex shader
'''

fragment_shader = '''
// contenu du fragment shader
'''

shader_program = shaders.compileProgram(
    shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
    shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))


vertices = farray([
    0.6, 0.6, 0.0, 1.0,
    -0.6, 0.6, 0.0, 1.0,
    0.0, -0.6, 0.0, 1.0,
])


vertex_array_object = glGenVertexArrays(1)
glBindVertexArray(vertex_array_object)

vertex_buffer = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
glBufferData(GL_ARRAY_BUFFER, 48, vertices, GL_STATIC_DRAW)

glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 4, GL_FLOAT, False, 0, ctypes.c_void_p(0))

glBindBuffer(GL_ARRAY_BUFFER, 0)
glBindVertexArray(0)



# DÉBUT

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    

    # DESSIN  
    
    pygame.display.flip()
    
    clock.tick(60)
    
    glUseProgram(shader_program)
                         
    glBindVertexArray(vertex_array_object)		     
    glBindVertexArray(vertex_array_object)
    glBindVertexArray(0)
                         
    glUseProgram(0)  
    
pygame.quit()
