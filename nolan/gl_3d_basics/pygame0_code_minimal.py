#!coding: utf-8
from __future__ import print_function, division
from OpenGL.GL import *
from OpenGL.GL import shaders
# créer un compte sur github.com, fork gitub.com/robertvandeneynde/parascolaire-students, clone, modif, commit, push, pull request

import pygame
pygame.init()
#Code à vérifier... L'écran ne démarre pas correctement...

pygame.display.set_mode((700, 500), pygame.OPENGL | pygame.DOUBLEBUF)

NOIR = [0, 0, 0]
BLANC = [1, 1, 1]
ROUGE = [1, 0, 0]
VERT = [0, 1, 0]
BLEU = [0, 0, 1]


# DÉBUT

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    

    # DESSIN
    
    glUseProgram(shader_program)
    vertex_buffer = glGenBuffers(1)
    glBufferData(GL_ARRAY_BUFFER, 48, vertices, GL_STATIC_DRAW)
    #Mettre au début du code
    glBindVertexArray(vertex_array_object)
    # ici on fera un dessin opengl utilisant le vao et le shader program
    glBindVertexArray(0)
    
    #----------------------------------------------
    
    #Manipulation du VAO
    
    vertex_array_object = glGenVertexArrays(1)
    glBindVertexArray(vertex_array_object) # on sélectionne le vao "vertex_array_object"
    # manipulation vao
    glBindVertexArray(0)
    glEnableVertexAttribArray(0) # on active l'attribut 0
    glVertexAttribPointer(0, 4, GL_FLOAT, False, 0, ctypes.c_void_p(0)) # données par groupe de 4 Float dans l'attribut 0    
    
    #----------------------------------------------
    
    
    vertex_shader = '''
    // contenu du vertex shader
    '''
    
    fragment_shader = '''
    // contenu du fragment shader
    '''
    #Clairement du copier-coller, revérifier cela
    shader_program = shaders.compileProgram(
        shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
        shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))
    
    
    oglUseProgram(shader_program)

    glBindVertexArray(vertex_array_object)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glBindVertexArray(0)

    glUseProgram(0)
    
       
    vertices = farray([
        0.6, 0.6, 0.0, 1.0,
        -0.6, 0.6, 0.0, 1.0,
        0.0, -0.6, 0.0, 1.0,
    ])    
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
