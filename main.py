"""Arquivo principal que será interpretado pelo interpretador."""
import math


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    area = float(input('Digite quantos metros deseja pintar: '))
    volume = (area/6)*1.1
    qtd_latas = int(-(-volume//18))
    valor = qtd_latas*80
    print(f'O valor gasto comprando apenas latas é de R$ {valor:.2f}.')
    print(f'Serão necessárias {qtd_latas} latas.')
    volume = (area/6)*1.1
    qtd_gal =int(-(-volume//3.6))
    valor2 = qtd_gal*25
    print(f'O valor gasto comprando apenas galões é de R$ {valor2:.2f}.')
    print(f'Serão necessários {qtd_gal} galões.')
    volume = (area/6)*1.1
    qtd_latas_int = int(volume//18)
    vol_rest_l = volume%18
    qtd_latas = int(-(-vol_rest_l//18))
    qtd_gal = int(-(-vol_rest_l//3.6))
    qtd_latas = int(qtd_latas_int + (qtd_gal>80/25) * qtd_latas)
    qtd_gal = int((qtd_gal<=80/25) * qtd_gal)
    total_1 = 80*qtd_latas_int + 25*qtd_gal
    total_2 = 80*qtd_latas_int + 80*qtd_latas
    valor3 = min(total_1,total_2)
    print(f'O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ {valor3:.2f}.')
    print(f'Serão necessárias {qtd_latas} latas e {qtd_gal} galões.')



if __name__ == '__main__':
    main()
