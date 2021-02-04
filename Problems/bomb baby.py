'''
def solution(m, f):
    seen = set()
    target = (int(m), int(f))
    start = (1, 1)
    generations = set([start])
    count = 0

    while generations:
        next_generations = set()
        if target in generations:
            return str(count)

        for mach, facula in generations:
            temp = mach + facula
            if temp <= target[0]:
                s = (temp, facula)
                if s not in seen:
                    next_generations.add((temp, facula))
            if temp <= target[1]:
                s = (mach, temp)
                if s not in seen:
                    next_generations.add((mach, temp))

        generations = next_generations
        count += 1

    return 'impossible'
'''

def solution(m, f):
    target = (int(m), int(f))
    mach, facula = target
    count = 0

    while mach != facula:
        if mach > facula:
            number_subtractions = (mach - facula) // facula
            number_subtractions += ((mach - facula) % facula > 0)
            count += number_subtractions
            mach = mach - number_subtractions * facula

        elif facula > mach:
            number_subtractions = (facula - mach) // mach
            number_subtractions += ((facula - mach) % mach > 0)
            count += number_subtractions
            facula = facula - number_subtractions * mach


    return str(count) if (mach, facula) == (1, 1) else 'impossible'

print(solution(2, 1))
print(solution(19, 10))
print(solution(99, 199))
print(solution(2, 4))
