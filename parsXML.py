import xml.etree.ElementTree as ET
import xlsxwriter

tree = ET.parse(r'C:\Users\user\Desktop\Container_10009100_010823_5008361 (1).XML')
root = tree.getroot()


namespaces = {'xmlns1':'urn:customs.ru:Information:ExchangeDocuments:ED_Container:5.21.0',
              'cat_ru1':'urn:customs.ru:CommonAggregateTypes:5.21.0',
              'xmlns2':'urn:customs.ru:Information:CustomsDocuments:ESADout_CU:5.21.0',
              'clt_ru':'urn:customs.ru:CommonLeafTypes:5.10.0',
              'cat_ru2':'urn:customs.ru:CommonAggregateTypes:5.21.0',
              'catESAD_cu':'urn:customs.ru:CUESADCommonAggregateTypesCust:5.21.0',
            }
tagNameTotNum = root.findall('.//catESAD_cu:TotalGoodsNumber', namespaces)
tagNamePackNum = root.findall('.//catESAD_cu:TotalPackageNumber', namespaces)
descGoods = root.findall('.//xmlns2:ESADout_CUGoods/'
                         'catESAD_cu:GoodsDescription', namespaces)
descGoodsGroup = root.findall('.//xmlns2:ESADout_CUGoods/'
                              'catESAD_cu:GoodsGroupDescription/'
                              'catESAD_cu:GoodsDescription', namespaces)
GoodsQuantGroup = root.findall('.//xmlns2:ESADout_CUGoods/'
                               'catESAD_cu:GoodsGroupDescription/'
                               'catESAD_cu:GoodsGroupInformation/'
                               'catESAD_cu:GoodsGroupQuantity/'
                               'catESAD_cu:GoodsQuantity', namespaces)
SupplGoodsQuant = root.findall('.//xmlns2:ESADout_CUGoods/'
                               'xmlns2:SupplementaryGoodsQuantity/'
                               'cat_ru2:GoodsQuantity', namespaces)
SupplGoodsQuant1 = root.findall('.//xmlns2:ESADout_CUGoods/'
                               'xmlns2:SupplementaryGoodsQuantity1/'
                               'cat_ru2:GoodsQuantity', namespaces)

a = 1

# for i in SupplGoodsQuant1:
#     if i.text is None:
#         SupplGoodsQuant1[i] = SupplGoodsQuant1[i].append('')
#     else:


GoodsNum = root.findall('.//catESAD_cu:GoodsNumeric', namespaces)
GrossWeightQuan = root.findall('.//catESAD_cu:GrossWeightQuantity', namespaces)
GoodsTNVEDCode = root.findall('.//catESAD_cu:GoodsTNVEDCode', namespaces)





workbook = xlsxwriter.Workbook('234.xlsx')
worksheet = workbook.add_worksheet('1')

worksheet.write('A1', 'GoodsNum')
worksheet.write('B1', 'descGoods')
worksheet.write('C1', 'descGoodsGroup')
worksheet.write('D1', 'GoodsQuantGroup')
worksheet.write('E1', 'SupplGoodsQuant')
worksheet.write('F1', 'SupplGoodsQuant1')
worksheet.write('G1', 'GrossWeightQuan')
worksheet.write('H1', 'GoodsTNVEDCode')

rowIndex = 2

for row in range(len(GoodsNum)):
    worksheet.write('A' + str(rowIndex), GoodsNum[row].text)
    worksheet.write('B' + str(rowIndex), descGoods[row].text)
    # worksheet.write('C' + str(rowIndex), descGoodsGroup[row].text)
    # worksheet.write('D' + str(rowIndex), GoodsQuantGroup[row].text)
    # worksheet.write('E' + str(rowIndex), SupplGoodsQuant[row].text)
    # worksheet.write('F' + str(rowIndex), SupplGoodsQuant1[row].text)
    # worksheet.write('G' + str(rowIndex), GrossWeightQuan[row].text)
    # worksheet.write('H' + str(rowIndex), GoodsTNVEDCode[row].text)

    rowIndex += 1

workbook.close()

