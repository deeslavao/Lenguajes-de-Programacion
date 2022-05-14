palabras_reservadas = [
    'ant', 'all', 'big', 'bus', 'boss', 'cat', 'cow'
]

tokens_especiales = { 
    }

gramatica = {
    'A': [['B','C'],['ant','A','all']],
    'B': [['big','C'],['bus','A','boss'],['epsilon']],
    'C': [['cat'],['cow']]
}