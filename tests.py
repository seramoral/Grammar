# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 11:55:44 2023

@author: Serafin
"""

from grammar import GenerativeGrammar

path = "grammar_proof.txt"
generated_grammar = GenerativeGrammar.readGrammar(path)
#generated_grammar.deleteUselessSymbolsProductions()
# out_file ="grammar_written.txt" 
# generated_grammar.writeGrammar(out_file)
"""
word = "<A1>aab<A2>"
production_to_apply = generated_grammar.production_rules[0]
derivated_word = generated_grammar.applyProductionRule(word, 0,3,production_to_apply)
print(derivated_word) """


"""
linear_right = generated_grammar.linearRight()
print(linear_right) """

"""
linear_left = generated_grammar.linearLeft()
print(linear_left) """

#deleteUselessSymbolsProductions()
#print(generated_grammar) 


#empty_languaje = generated_grammar.emptyLanguaje()
# print(empty_languaje)

""" generated_grammar.deleteNullProdutions()
print(generated_grammar) """

"""generated_grammar.deleteUnitaryProdutions()
print(generated_grammar) """ 

""" generated_grammar.transformChomsky()
print(generated_grammar) """

""" generated_grammar.transformGreibach()
word1 = "ab"
belonging_word1 = generated_grammar.wordBelongsGreibach(word1)
print(belonging_word1)
#generated_grammar.writeGrammar(out_file)"""

""" path2 = "grammar_proof2.txt"
generated_grammar2 = GenerativeGrammar.readGrammar(path2)
grammar_union = generated_grammar.unionGrammar(generated_grammar2)
out_file_union = "grammar_union_written.txt"
grammar_union.writeGrammar(out_file_union) """

""" grammar_concatenation = generated_grammar.concatenationGrammar(generated_grammar2)
out_file_concatenation = "grammar_concatenation_written.txt"
grammar_concatenation.writeGrammar(out_file_concatenation) """

""" grammar_clausure = generated_grammar.clausureGrammar()
out_file_clausure = "grammar_clausure_written.txt"
grammar_clausure.writeGrammar(out_file_clausure) """

"""
empty_languaje = generated_grammar.emptyLanguaje()
print(empty_languaje)

infinity_languaje = generated_grammar.infinityLanguaje()
print(infinity_languaje) """
word = 'baa'
belongs = generated_grammar.checkBelongingEarly(word)
print(belongs)

 