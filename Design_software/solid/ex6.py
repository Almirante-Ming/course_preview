from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar(self, destinatario, mensagem):
        pass

class EmailService(Notificador):
    def enviar(self, destinatario, mensagem):
        print(f"Enviando email para {destinatario}: {mensagem}")

class SMSService(Notificador):
    def enviar(self, destinatario, mensagem):
        print(f"Enviando SMS para {destinatario}: {mensagem}")

class Notificacao:
    def __init__(self, notificador: Notificador):
        self.notificador = notificador

    def notificar(self, destinatario, mensagem):
        self.notificador.enviar(destinatario, mensagem)

# ------------------------------------------------------------------
notificacao_email = Notificacao(EmailService())
notificacao_email.notificar("usuario@exemplo.com", "Bem-vindo!")

notificacao_sms = Notificacao(SMSService())
notificacao_sms.notificar("123456789", "Seu código é 4567")
