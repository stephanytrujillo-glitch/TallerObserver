from observer_practice.canal import CanalNoticias
from observer_practice.suscriptores import SuscriptorEmail, SuscriptorSMS


def main():
    canal = CanalNoticias("Python al dia")
    ana = SuscriptorEmail("Ana")
    luis = SuscriptorSMS("Luis")

    canal.suscribir(ana)
    canal.suscribir(luis)
    canal.publicar("Nueva clase sobre patrones de diseno")

    print(ana.mensajes)
    print(luis.mensajes)


if __name__ == "__main__":
    main() 