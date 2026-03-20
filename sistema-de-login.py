usuario = input('Crie seu usuário: ') #hora de criar seu usuario.
senha = input('Crie sua senha: ') #hora de criar sua senha.

print('Login e senha criado com sucesso!')

tentativas = 0 #tentativas inicialmente definida em 0.

while tentativas < 3: #tentativas totais definida em 3.
    user = input('Qual seu usuário?: ') #hora de digitar seu usuario criado.
    password = input('Qual sua senha?: ') #hora de digitar sua senha criada.

    if usuario == user and senha == password: #se seu login for igual ao usuario criado, e sua senha digitada for igual a criado. Seu login foi efetuado.
        print('Login efetuado com sucesso!' )
        exit(0)
    elif usuario != user or senha != password and tentativas == 2: #se existir algo diferente, e as tentativas for maior do que 2, vc bloqueou o sistema.
        print('Login bloqueado, tente novamente em 10 minutos.' )
        exit(0)
    else: #se existir algo diferente, e as tentativas for menor do que 3, vc terá uma nova tentativa.
        print('Tente novamente.')
        tentativas += 1