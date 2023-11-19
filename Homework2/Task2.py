# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и *произведение дробей. Для проверки своего кода используйте модуль fractions.
import fractions
import math


def denominator_not_different_summ(new_fraction_list1: list[int], new_fraction_list2: list[int]) -> str:
    numerator = new_fraction_list1[0] + new_fraction_list2[0]
    if numerator == (new_fraction_list1[1]):
        new_fraction = '1'
        return new_fraction
    new_fraction = str(numerator) + '/' + str(new_fraction_list1[1])
    return new_fraction


def denominator_different_summ(new_fraction_list1: list[int], new_fraction_list2: list[int]) -> str:
    nok = math.lcm(new_fraction_list1[1], new_fraction_list2[1])
    add_multiplier_1 = nok // new_fraction_list1[1]
    add_multiplier_2 = nok // new_fraction_list2[1]
    numerator_1 = new_fraction_list1[0] * add_multiplier_1
    numerator_2 = new_fraction_list2[0] * add_multiplier_2
    numerator = numerator_1 + numerator_2
    nod = math.gcd(numerator, nok)
    if type(nod) == int:
        numerator = numerator // nod
        nok = nok // nod
    new_fraction = str(numerator) + '/' + str(nok)
    return new_fraction


def fraction_proz(new_fraction_list1: list[int], new_fraction_list2: list[int]) -> str:
    numerator = new_fraction_list1[0] * new_fraction_list2[0]
    denominator = new_fraction_list1[1] * new_fraction_list2[1]
    nod = math.gcd(numerator, denominator)
    if type(nod) == int:
        numerator = numerator // nod
        denominator = denominator // nod
    new_fraction = str(numerator) + '/' + str(denominator)
    return new_fraction


fraction_1 = input()
fraction_2 = input()

fraction_list1 = fraction_1.split('/')
fraction_list2 = fraction_2.split('/')

fraction_list1 = [int(i) for i in fraction_list1]
fraction_list2 = [int(i) for i in fraction_list2]

frac_1 = fractions.Fraction(fraction_list1[0], fraction_list1[1])
frac_2 = fractions.Fraction(fraction_list2[0], fraction_list2[1])
frac_summ = str(frac_1 + frac_2)
frac_proz = str(frac_1 * frac_2)

if fraction_list1[1] == fraction_list2[1]:
    if frac_summ == denominator_not_different_summ(fraction_list1, fraction_list2):
        print(f'{True}\t{frac_summ = }\t{denominator_not_different_summ(fraction_list1, fraction_list2) = }')
    else:
        print(f'{False}\t{frac_summ = }\t{denominator_not_different_summ(fraction_list1, fraction_list2) = }')
else:
    if frac_summ == denominator_different_summ(fraction_list1, fraction_list2):
        print(f'{True}\t{frac_summ = }\t{denominator_different_summ(fraction_list1, fraction_list2) = }')
    else:
        print(f'{False}\t{frac_summ = }\t{denominator_different_summ(fraction_list1, fraction_list2) = }')

if frac_proz == fraction_proz(fraction_list1, fraction_list2):
    print(f'{True}\t{frac_proz = }\t{fraction_proz(fraction_list1, fraction_list2) = }')
else:
    print(f'{False}\t{frac_proz = }\t{fraction_proz(fraction_list1, fraction_list2) = }')