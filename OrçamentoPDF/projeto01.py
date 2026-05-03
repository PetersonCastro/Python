from fpdf import FPDF

projeto = input("Digite a Descrição do projeto: ")
horas_previstas = input("Digite a quantidade de horas previstas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo = input("Digite prazo estimado: ")

valor_total = int(horas_previstas)*int(valor_hora)

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial", size=15, style="B")

pdf.image(r"C:\Users\Pichau\OneDrive\Documentos\Peterson - Programação\Python\OrçamentoPDF\template.png", x=0, y=0 , w=210, h=297)

pdf.text(115, 155, projeto.upper())
pdf.text(115, 175, horas_previstas)
pdf.text(115, 194, valor_hora)
pdf.text(115, 213, prazo)
pdf.text(115, 230, str(valor_total))

pdf.output("Orçamento.pdf")
print("Orçamento gerado com sucesso!!!")
