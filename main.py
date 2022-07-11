from fpdf import FPDF as PDF

pdf = PDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

pdf.image(name='tiger.jpeg', w=80, h=50)

pdf.set_font('Arial', size=24, style='B')
pdf.cell(w=0, h=50, txt='Malayan Tiger', align='C', ln=1)

pdf.set_font(family='Times', size=14, style='B')
pdf.cell(w=0, h=15, txt='Description', align='L', ln=1)

malayan_tiger_text = "The Malayan tiger is a tiger from a specific population of the Panthera tigris tigris " \
                     "subspecies that is native to Peninsular Malaysia.[1] This population inhabits the southern and " \
                     "central parts of the Malay Peninsula and has been classified as critically endangered on the " \
                     "IUCN Red List since 2015. As of April 2014, the population was estimated at 80 to 120 mature " \
                     "individuals with a continuous declining trend.[2]\n\nIn the Malay language, the tiger is called " \
                     "harimau, also abbreviated to rimau.[3] It is also known as the southern Indochinese tiger, " \
                     "to distinguish it from tiger populations in northern parts of Indochina, which are genetically " \
                     "different to this population.[4] "

pdf.set_font(family='Times', size=12)
pdf.multi_cell(w=0, h=15, txt=malayan_tiger_text)

pdf.output('tiger.pdf')