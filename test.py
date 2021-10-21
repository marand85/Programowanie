# Obliczam jak przygotować solankę o zadanym stężeniu soli przy zadanej ilości wody.
# Czyli znam ilość wody i jakie ma być stężenie soli, a obliczam ile soli należy dodać.

try:
    woda_str = ""
    while woda_str != 'exit':
        woda_str = input("Podaj ilość wody w gramach (1 litr = 1000g):\n")
        if woda_str == 'exit':
            break
        woda = float(woda_str)
        stezenie = float(input("Podaj jakie ma byc stezenie w %:\n"))
        """
        sol / (woda + sol) = stezenie/100.
        sol = (woda + sol)(stezenie/100.)
        sol = woda*stezenie/100. + sol*stezenie/100.
        sol - sol*stezenie/100. = woda*stezenie/100.
        sol (1 - stezenie/100.) = woda*stezenie/100.
        sol = (woda*stezenie/100.)/(1 - stezenie/100.)
        """
        sol = (woda*stezenie/100.)/(1 - stezenie/100.)
        format_sol = "{:.2f}".format(sol)
        format_woda = "{:.0f}".format(woda)
        format_stezenie = "{:.2f}".format(stezenie)
        print("\nDo",str(format_woda)+"g wody należy dodać",str(format_sol)+"g soli, aby uzyskać",str(format_stezenie)+"% solankę.\n")
except:
    print("Błędne dane wejściowe.")