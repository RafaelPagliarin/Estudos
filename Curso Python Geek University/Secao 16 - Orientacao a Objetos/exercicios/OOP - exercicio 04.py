class Televisao:
    def __init__(self, volume=10, canal=3):
        self.volume = volume
        self.canal = canal

    def set_canal(self, valor):
        self.canal = valor

    def set_volume(self, valor):
        self.volume = valor

    def get_volume(self):
        return self.volume

    def get_canal(self):
        return self.canal


class ControleRemoto:
    def __init__(self, tv):
        self.tv = tv

    def mudar_canal(self, valor):
        if valor == 1:
            self.tv.set_canal(self.tv.get_canal() + 1)
        elif valor == -1:
            self.tv.set_canal(self.tv.get_canal() - 1)
        else:
            print('Erro, apenas 1 canal por vez.')

    def mudar_volume(self, valor):
        if valor == 1:
            self.tv.set_volume(self.tv.get_volume() + 1)
        elif valor == -1:
            self.tv.set_volume(self.tv.get_volume() - 1)
        else:
            print('Erro, apenas 1 volume por vez')


televisao1 = Televisao()
controle1 = ControleRemoto(televisao1)

print(f'Volume: {televisao1.get_volume()} , Canal: {televisao1.get_canal()}')

controle1.mudar_volume(-1)
controle1.mudar_canal(1)

print(f'Volume: {televisao1.get_volume()} , Canal: {televisao1.get_canal()}')

