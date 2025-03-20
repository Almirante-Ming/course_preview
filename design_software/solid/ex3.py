from abc import abstractmethod, ABC

class Relatorio(ABC):    
    @abstractmethod
    def gerar_relatorio():
        pass
    
class RelatorioPdf(Relatorio):
    def gerar_relatorio(self):
        return "gerando relatorio em pdf"
    
    
class RelatorioCsv(Relatorio):
    def gerar_relatorio(self):
        return "gerando relatorio em csv"   

class RelatorioHtml(Relatorio):
    def gerar_relatorio(self):
        return "gerando relatorio em html"
    
class RelatorioXlsx(Relatorio):
    def gerar_relatorio(self):
        return "gerando relatorio em excel"
    
class GeradorRelatorios:
    def __init__(self, relatorio: Relatorio):
        self.relatorio = relatorio

    def gerar_relatorio(self):
        return self.relatorio.gerar_relatorio()
    
# ----------------------------------------------
gerador_pdf = GeradorRelatorios(RelatorioPdf())
print(gerador_pdf.gerar_relatorio())

gerador_csv = GeradorRelatorios(RelatorioCsv())
print(gerador_csv.gerar_relatorio())

gerador_html = GeradorRelatorios(RelatorioHtml())
print(gerador_html.gerar_relatorio())

gerador_excel = GeradorRelatorios(RelatorioXlsx())
print(gerador_excel.gerar_relatorio())