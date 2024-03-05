from tabulate import tabulate

class User:
    # Dummy database user
    data = {
        1 : ['Randy', 'Basic Plan', 12, 'randy123'],
        2 : ['Dian', 'Standard Plan', 24, 'dian123'],
        3 : ['Kirana', 'Premium Plan', 4, 'kirana123'],
        4 : ['Arkan', 'Premium Plan', 10, 'arkan123']
    }

    # Benefit Ranflix
    header = ['Basic Plan', 'Standard Plan', 'Premium Plan', 'Services']
    table_benefit = [
        [True, True, True, 'can_stream'],
        [True, True, True, 'can_download'],
        [True, True, True, 'has_SD'],
        [True, True, False, 'has_SD'],
        [False, False, True, 'has_UHD'],
        [1, 2, 4, 'num_of_devices'],
        ['3rd party movie only', 'Basic Plan Content + Sports (F1, Football, Basketball)',
         'Basic Plan + Standard Plan + PacFlix Original Series or Movie', 'content'],
        [120_000, 160_000, 200_000, 'price']
    ]

    def __init__ (self):
        '''
        init class user
        '''
        self.username = None
        self.duration = None
        self.current_plan = None
        self.code_refferal = None

    def login (self, username):
        '''
        Fungsi untuk melakukan login

        Parameters
        ----------
        Username : username yang digunakan untuk login

        Method
        -------
        set durration, current plan, dan code refferal sesuai dummy data dari list dictionary

        Output
        ------
        tidak ada
        '''
        self.username = username

        for key, value in self.data.items():
            if value[0] == username:
                self.duration = value[2]
                self.current_plan = value[1]
                self.code_refferal = value[3]
                break
            else:
                self.duration = None
                self.current_plan = None
                self.code_refferal = None

    def check_benefit(self):
        '''
        Fungsi untuk menampilkan semua list benefit

        Parameters
        -----------
        tidak ada

        Method
        -------
        Print list header dan list table benefit memakai tabulate

        Output
        -------
        list semua benefit Ranflix
        '''
        print ("Ranflix Plan List")
        print (tabulate(self.table_benefit, self.header))

    def check_plan (self):
        '''
        Fungsi untuk melakukan check plan user

        Parameters
        -----------
        tidak ada

        Method
        -------
        Melakukan looping untuk mencari plan sesuai dengan data login

        Output
        -------
        list plan user : menampilkan plan yang dimiliki user yang sudah login
        '''
        print (f"Plan dari user {self.username}")
        print ('')
        print (f"Plan = {self.current_plan}")
        print (f"Duration = {self.duration} Bulan")
        print ('')

        if self.current_plan in self.header:
            if self.current_plan == 'Basic Plan':
                header = ['Basic Plan', 'Services']
                benefit = [[row[0], row[-1]] for row in self.table_benefit] # Use list comprehension

            elif self.current_plan == 'Standard Plan':
                header = ['Standard Plan', 'Services']
                benefit = []
                for row in self.table_benefit: # Use for loop standard
                    benefit.append([row[1], row[-1]])

            elif self.current_plan == 'Premium Plan':
                header = ['Premium Plan', 'Services']
                benefit = []
                for row in self.table_benefit: # Use for loop standard
                    benefit.append([row[2], row[-1]])

            print (tabulate(benefit, header))

        else:
            print ('Plan tidak tersedia')

    def upgrade_plan (self, new_plan):
        '''
        Fungsi untuk melakukan upgrade plan

        Parameters
        -----------
        New Plan : Nama plan baru yang ingin dimiliki

        Method
        -------
        Tidak bisa downgrade plan atau memilih plan yang sama
        Jika duration > 12 maka mendapatkan diskon 50%

        Output
        -------
        Harga beserta informasi plan baru
        '''
        self.new_plan = new_plan
        idx_current_plan = self.header.index(self.current_plan)
        idx_new_plan = self.header.index(new_plan)

        if idx_current_plan > idx_new_plan:
            print ('Tidak bisa downgrade')

        elif idx_current_plan == idx_new_plan:
            print ('Anda sudah memiliki plan ini')
        
        else:
            self.current_plan = new_plan
            if self.duration > 12:
                percentage_discount = 0.5
                discount = self.table_benefit[7][idx_new_plan] * percentage_discount
                total = self.table_benefit[7][idx_new_plan] - discount
            else:
                total = self.table_benefit[7][idx_new_plan]
            print (f'Selamat anda upgrade ke plan {new_plan}, bayar {total}')

    def subscribe (self, plan, code_refferal):
        '''
        Fungsi untuk melakukan pembelian paket

        Parameters
        -----------
        plan : nama plan yang ingin dimiliki
        code refferal : code refferal yang ingin digunakan, diambil dari existing user
        
        method
        -------
        Jika punya code refferal dan valid, maka mendapatkan diskon 4% of harga paket

        Output
        -------
        Informasi plan yang ingin dimiliki beserta total yang harus dibayar user
        '''
        self.current_plan = plan
        self.duration = 1
        self.code_refferal = self.username + '123'
        
        if plan in self.header:
            list_refferal = []
            for key, value in self.data.items():
                list_refferal.append(value[-1])
            
            idx_plan = self.header.index(plan)
            
            if code_refferal in list_refferal:
                percentage_discount = 0.04
                discount = self.table_benefit[7][idx_plan] * percentage_discount
                total = self.table_benefit[7][idx_plan] - discount
            else:
                total = self.table_benefit[7][idx_plan]
            
            print (f"Selamat, anda telah berlangganan {plan}, bayar Rp {total}")

        else:
            print ('Plan tidak tersedia')