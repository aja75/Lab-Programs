import PySimpleGUI as sg

sg.theme('Default1')

tissue_box = [
    [sg.Checkbox("Breast", key='BREAST'), sg.Checkbox("Pancreas", key='PANCREAS'), sg.Checkbox("Skin", key='SKIN'),
     sg.Checkbox("Prostate", key='PROSTATE')],
    [sg.Checkbox("Liver", key='LIVER'), sg.Checkbox("Testis", key='TESTIS'), sg.Checkbox("Bladder", key='BLADDER'),
     sg.Checkbox("Lung", key='LUNG')],
    [sg.Checkbox("Intestine", key='INTESTINE'), sg.Checkbox("Colon", key='COLON'), sg.Checkbox("Uterus", key='UTERUS'),
     sg.Checkbox("Brain", key='BRAIN')],
    [sg.Checkbox("Kidney", key='KIDNEY'), sg.Checkbox("Cervix", key='CERVIX'), sg.Checkbox("Stomach", key='STOMACH'),
     sg.Checkbox("Thyroid", key='THYROID')],
    [sg.Text("Upload Expression screenshot"), sg.FileBrowse(key='Expression_SC', button_color="#28579C")]
    ]

lnc_class = [
    [sg.Radio("sense", 'CLASS', key="SENSE", default=True),
     sg.Radio("anti-sense", 'CLASS', key="ANTI-SENSE"),
     sg.Radio("bidirectional", 'CLASS', key="BIDIRECTIONAL")],
    [sg.Radio("intronic", 'CLASS', key="INTRON"),
     sg.Radio("intergenic", 'CLASS', key="INTERGENIC"),
     sg.Radio("unknown", 'CLASS', key="UNKNOWN")]
]

data = []

CpG_Island = [
    [sg.Text("Position: "), sg.Input(key='POSITION', size=8, tooltip="If N/A input NULL")],
    [sg.Text("Size: "), sg.Input(key='SIZE', size=8, tooltip="If N/A input NULL")],
    [sg.Text("CpG Count: "), sg.Input(key='CPG_CNT', size=8, tooltip="If N/A input NULL")],
    [sg.Text("Upload CpG island screenshot"), sg.FileBrowse(key='CpG_SC', button_color="#28579C")]
]

promoter = [
    [sg.Text('Position: '), sg.Input(key='P_POSITION', size=5)],
    [sg.Text('Promoter ID: '), sg.Input(key='P_ID', size=5)],
    [sg.Text("Upload Promoter screenshot"), sg.FileBrowse(key='PROMOTER_SC', button_color="#28579C")]
]

TSS = [
    [sg.Text('Position: '), sg.Input(key='TSS_POSITION', size=5)],
    [sg.Text('Strand: '), sg.Input(key='TSS_STRAND', size=5)],
    [sg.Text('ITEM ID: '), sg.Input(key='TSS_ID', size=8)],
    [sg.Text("Upload TSS screenshot"), sg.FileBrowse(key='TSS_SC', button_color="#28579C")]
]

TAF_list = [
    [sg.Input(key='TAFs', size=40, tooltip="separate TAFs with comma")],
    [sg.Text("Upload TAF screenshot"), sg.FileBrowse(key='TAF_SC', button_color="#28579C")]
]

font = ("Roboto", 12)

layout = [
    [sg.Column([
        [sg.Text('UCSC GUI for lncRNA sgRNA v23_06_08', font=font)],
        [sg.Text("Developed by Anthony Aceto")],
        [sg.Text("_"*50)],
        [sg.Text("Input Data From UCSC", font=font)],
        [sg.Text("Chromosome of lncRNA: "), sg.Input(key='lnc_CHR', size=5)],
        [sg.Text("Chromosome Band: "), sg.Input(key='lnc_BAND', size=8)],
        [sg.Text("Gene Start: "), sg.Input(key='lnc_START', size=8)],
        [sg.Text("Gene End: "), sg.Input(key='lnc_END', size=8)],
        [sg.Text("Gene Name: "), sg.Input(key='lnc_NAME', size=12)],
        [sg.Text("ENSEMBL Gene ID: "), sg.Input("ENSG", key='lnc_ENSEMBL', size=20)],
        [sg.Text("ENSEMBL Transcript ID: "), sg.Input("ENST", key='lnc_ENSEMBL_T', size=20)],
        [sg.Frame("Select lncRNA Class Type", lnc_class)],
        [sg.Text("Upload GTEx screenshot"), sg.FileBrowse(key='GTEx_SC', button_color="#28579C")],

        [sg.Text("_"*50)],
        [sg.Text("Data From Wang et al., 2018")],
        [sg.Text("Select lncRNA is Epigenetics", font=font)],
        [sg.Radio("Activated", "epigenetics", default=True, key='EA'), sg.Radio("Silenced", "epigenetics", key='ES'),
         sg.Radio("N/A", "epigenetics", key='NA')],
        [sg.Text("Input Expression Value: "), sg.Input(key='EXP_VAL', size=5, tooltip="If N/A input NULL")],

        [sg.Text("_"*50)],
        [sg.Text("Data From UCSC GTEx RNA-seq")],
        [sg.Frame("Select Expression Tissues:", tissue_box, font=font)],

        [sg.Text("_"*50)],
        [sg.Frame("Input Promoter Values:", promoter, font=font)],
        [sg.Frame("Input TSS Values :", TSS, font=font)],
        [sg.Frame("Input JASPAR TAFs that Overlap Promoter:", TAF_list)],
        [sg.Frame("Input CpG Island Nearest to Promoter:", CpG_Island)],
        [sg.FolderBrowse("File Output", button_color='#28579C', key='OUTPUT')],
        [sg.Submit(button_color='#28579C'), sg.Quit(button_color='#9C3C28')]],
        scrollable=True, vertical_scroll_only=True, size=(400, 500))],

]
