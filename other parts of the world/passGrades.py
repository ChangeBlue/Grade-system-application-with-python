############################################################################_FINAL GRADES FUNCTION_#################################################################################
## AUTHOR: _RAAM1_
## VESRION: 1.1
####################################################################################################################################################################################


############################################################################_FINAL GRADES FUNCTION_#################################################################################
## AUTHOR: _RAAM1_
## VESRION: 1.1

Final = 2
grades = 0

student1 = ''
student2 = ''
student3 = ''
student4 = ''

print('Here you will know if the student passed or not')
print('the grades that will be tested are Math, Science, First Language, Religion, Social studies, Art, English.')
print('this program will turn 0 to 100 grades into A, B, C, D, E and F')

##################################################################################_MATH_############################################################################################

print('Math\n \n')
print('What was the grade for math in the first term (1 to 100)')
Gmath = int(input())
print('What was the grade for math in the second term (1 to 100)')
Gmath2 = int(input())
Cmath = Gmath + Gmath2
Fmath = Cmath / Final
print(f'Final grade in math is {Fmath} \n \n')

##################################################################################_SCIENCE_#########################################################################################

print('Science\n \n')
print('What was the grade for Science in the first term (1 to 100)')
Gscience = int(input())
print('What was the grade for Science in the second term (1 to 100)')
Gscience2 = int(input())
Cscience = Gscience + Gscience2
Fscience = Cscience / Final
print(f'Final grade in Science is {Fscience}\n \n')

##################################################################################_FIRST LANGUAGE_##################################################################################

print('First Language\n \n')
print('What was the grade for First Language in the first term (1 to 100)')
GfirstLanguage = int(input())
print('What was the grade for First Language in the second term (1 to 100)')
GfirstLanguage2 = int(input())
CfirstLanguage = GfirstLanguage + GfirstLanguage2
FfirstLanguage = CfirstLanguage / Final
print(f'Final grade in firstLAnguage is {FfirstLanguage}\n \n')

##################################################################################_RELIGION_########################################################################################

print('Religion\n \n')
print('What was the grade for Religion in the first term (1 to 100)')
Greligion = int(input())
print('What was the grade for Religion in the second term (1 to 100)')
Greligion2 = int(input())
Creligion = Greligion + Greligion2
Freligion = Creligion / Final
print(f'Final grade in religion is {Freligion}\n \n')

##################################################################################_SOCIAL STUDIES_##################################################################################

print('Social studies\n \n')
print('What was the grades for Social studies in the first term (1 to 100)')
GsocialStudies = int(input())
print('what was the grades for Social studies in the second term (1 to 100)')
GsocialStudies2 = int(input())
Csocialstudies = GsocialStudies + GsocialStudies2
Fsocialstudies = Csocialstudies / Final
print(f'Final grade in Social studies is {Fsocialstudies}\n \n')

##################################################################################_ART & CRAFTS_####################################################################################

print('Arts & crafts \n \n')
print('What was the final grades for Arts & crafts in the first term (1 to 100)')
Gart = int(input())
print('what was the final grades for Arts & crafts in the second term (1 to 100)')
Gart2 = int(input())
Cart = Gart + Gart2
Fart = Cart / Final
print(f'Final grade in Arts & crafts is {Fart}\n \n')

##################################################################################_ENGLISH_#########################################################################################

print('English Language \n \n')
print('what was the final grades for Egnlish in the first term (1 to 100)')
Genglish = int(input())
print('what was the final grades for English in the second term (1 to 100)')
Genglish2 = int(input())
Cenglish = Genglish + Genglish2
Fenglish = Cenglish / Final
print(f'Final grade in English Language is {Fenglish}\n \n')

final_grade = str()
def calculate_grade(grade):
    if grade = 100:
        final_grade = 'A+'
    elif grade >= 93:
        final_grade = 'A'
    elif grade >= 85:
        final_grade = 'B'
    elif grade >= 74:
        final_grade = 'C'
    elif grade >= 67:
        final_grade = 'D'
    else:
        final_grade = 'F'
    return final_grade

_MATH_ = calculate_grade(Fmath)

_SCIENCE_ = calculate_grade(Fscience)

_FIRSTLANGUAGE_ = calculate_grade(FfirstLanguage)

_RELIGION_ = calculate_grade(Freligion)

_SOCIAL_ = calculate_grade(Fsocialstudies)

_ART_ = calculate_grade(Fart)

_ENGLISH_ = calculate_grade(Fenglish)

print('=======================Final grades in the YEAR: ========================= \n \n')
print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
print('* \t \t \t \t \t \t \t \t*')
print(f'*  \t \t Final grade in math is {_MATH_}\t \t \t*')
print('* \t \t \t \t \t \t \t \t*')
print('* \t \t \t \t \t \t \t \t*')
print(f'*  \t \t Final grade in Science is {_SCIENCE_} \t \t \t*')
print('* \t \t \t \t \t \t \t \t*')
print('* \t \t \t \t \t \t \t \t*')
print(f'*  \t \t Final grade in First Language is {_FIRSTLANGUAGE_} \t \t*')
print('* \t \t \t \t \t \t \t \t*')
print('* \t \t \t \t \t \t \t \t*')
print(f'*  \t \t Final grade in Religion is {_RELIGION_} \t \t \t*')
print('* \t \t \t \t \t \t \t \t*')
print('* \t \t \t \t \t \t \t \t*')
print(f'*  \t \t Final grade in Social studies is {_SOCIAL_} \t \t*')
print('* \t \t \t \t \t \t \t \t*')
print('* \t \t \t \t \t \t \t \t*')
print(f'*  \t \t Final grade in Art & crafts is {_ART_} \t \t*')
print('* \t \t \t \t \t \t \t \t*')
print('* \t \t \t \t \t \t \t \t*')
print(f'*  \t \t Final grade in English is {_ENGLISH_} \t \t \t*')
print('* \t \t \t \t \t \t \t \t*')
print('* \t \t \t \t \t \t \t \t*')
print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
