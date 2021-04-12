class bank_account():
    def __init__(self, start_balance):
        self.start_balance = start_balance
        self.limit = 10000
        self.balance = start_balance
        self.log_list = []
        self.log_limit = int(input('Какое количество последних транзакций вы хотите сохранить?\n'))
        while(1):
            self.choice = int(input('Выберите операцию: 1 - снятие наличных, 2 - начисление наличных на карту, 0 - чтобы закончить работу с банкоматом.\n'))
            if(self.choice == 1):
                self.withdraw(self.balance, self.log_list, self.log_limit)
            elif(self.choice == 2):
                self.assessment(self.balance, self.limit, self.log_list, self.log_limit)
            elif(self.choice == 0):
                break
        for self.elem in self.log_list:
            print(self.elem)
        
    def withdraw(self, balance, log_list, log_limit):
        if (self.balance <= 0):
            print('Недостаточно средств для проведения операции.')
            return
        self.govoryashaya_peremennaya = int(input('Введите сумму, которую хотите получить.\nСумма вывода не должна превышать ' + str(self.balance) + ' гривен.\n'))#Я не знал, какое название придумать для суммы снятия, но вы просили использовать говорящие переменные.
        if(self.balance < self.govoryashaya_peremennaya):
            print('Недостаточно средств для проведения операции.')
            return
        self.balance -= self.govoryashaya_peremennaya
        print(self.balance)
        if(len(self.log_list) < self.log_limit):
            self.log_list.append('Операция снятия - снято {0} грн - остаточный баланс {1} грн'.format(self.govoryashaya_peremennaya, self.balance))
        else:
            self.log_list.pop(0)
            self.log_list.append('Операция снятия - снято {0} грн - остаточный баланс {1} грн'.format(self.govoryashaya_peremennaya, self.balance))

    def assessment(self, balance, limit, log_list, log_limit):
        self.govoryashaya_peremennaya2 = int(input('Введите сумму, которую хотите начислить.\nСумма не должна превышать ' + str(self.limit) + ' гривен.\n'))#Я не знал, какое название придумать для начисления, чтобы не повторяться, но вы просили использовать говорящие переменные.
        if(self.govoryashaya_peremennaya2 >= self.limit):
            print('Сумма, которую вы собираетесь начислить, превышает лимит в ' + str(self.limit) + ' гривен')
            return
        self.balance += self.govoryashaya_peremennaya2
        print(self.balance)
        if(len(self.log_list) < self.log_limit):
            self.log_list.append('Операция начисления - начислено {0} грн - остаточный баланс {1} грн'.format(self.govoryashaya_peremennaya2, self.balance))
        else:
            self.log_list.pop(0)
            self.log_list.append('Операция начисления - начислено {0} грн - остаточный баланс {1} грн'.format(self.govoryashaya_peremennaya2, self.balance))

start_balance = int(input('Введите ваш баланс'))
bank_account(start_balance)
