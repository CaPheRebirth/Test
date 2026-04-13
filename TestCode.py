def test(a,b) :
    try :
        c = a + b
        if c < 18 :
            print('tre trau thi biet cai eo gi')
        elif c >= 18 :
            print('ok,may tai,gio thi bimbimbambam')
        else :
            print('wtf')
    except Exception as e :
        print(f'fix bug plss,bug is {e}')