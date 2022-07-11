import pandas
from fpdf import FPDF as PDF

attributes = {}
df = pandas.read_excel('Excel Data\\data.xlsx')
for index, row in df.iterrows():
    attributes.clear()
    name = row['name']
    attributes['Kingdom'] = row['kingdom']
    attributes['Phylum'] = row['phylum']
    attributes['Class'] = row['class']
    attributes['Order'] = row['order']
    attributes['Suborder'] = row['suborder']

    pdf = PDF(orientation='P', unit='pt', format='A4')
    pdf.add_page()
    pdf.set_font('Arial', size=24, style='B')
    pdf.cell(w=0, h=50, txt=name, align='C', ln=1)

    for names, attribute in attributes.items():
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=25, txt=names, align='L')
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=25, txt=attribute, align='L', ln=1)

    pdf.output('PDFs\\' + name + '.pdf')


