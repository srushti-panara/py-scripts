def func(name, *fav_subjects):
    print(name, 'likes to read')
    for subject in fav_subjects:
        print(subject)
func('Goransh', 'Mathematics', 'Android Programming')
func('Richa', 'C', 'Data structures','Design and Analysis of Algorithms')
func('Krish')