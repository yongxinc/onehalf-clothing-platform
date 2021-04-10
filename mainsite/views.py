from oscar.apps.offer.views import OfferListView as CoreOfferListView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import json
import sys
import requests
import selenium
from bs4 import BeautifulSoup
import json
from .catalogue import models
from django.views import generic
from django.views.generic import (
    ListView, CreateView
)

from mainsite import forms

# 賣家申請
from oscar.core.loading import (
    get_class, get_classes, get_model, get_profile_class)
PageTitleMixin, RegisterUserMixin = get_classes(
    'customer.mixins', ['PageTitleMixin', 'RegisterUserMixin'])

from django.views.generic import DetailView, TemplateView
from oscar.apps.catalogue.views import ProductDetailView as CoreProductDetailView

#我想試著Override這個view
# class ProductDetailView(CoreProductDetailView):
#     model = models.UNIQLOItem
#     def mo():
#         print(request)


def sellerApply(request):

    page_title = ('二手衣上架申請')
    active_tab = 'application'
    template_name = 'oscar/customer/application/application_page.html'
    sellerID = request.user
    # form = forms.SellerApplicationForm()
    print('apply is called')

    return render(request, template_name, locals())

#可參考 https://peilee-98185.medium.com/%E7%94%A8-django-form-%E5%BE%9E%E5%89%8D%E7%AB%AF%E5%82%B3%E8%B3%87%E6%96%99%E5%AD%98%E9%80%B2%E8%B3%87%E6%96%99%E5%BA%AB-c99723e63056
#裡面也有類別寫法
def getColorsFromJSON(item):
    universal_url =  'https://im.uniqlo.com/images/tw/uq/pc/goods/ITEMID/chip/COLORCODE_ITEMID.gif'
    item_url = universal_url.replace('ITEMID',item.UNIQLOID)
    # item_url = universal_url.replace('COLORCODE',item.UNIQLOID)


    color_dict = json.loads(item.ClothesColorJSON)

    color_name_list = []
    color_chip_list = []

    for key,value in color_dict.items():
        # color_name_list.append(key+' '+value)
        color_name_list.append(key)
        item_url=item_url.replace('COLORCODE',key)
        color_chip_list.append(item_url)
        item_url=item_url.replace(key,'COLORCODE')
    # print(color_name_list)
    # print(color_chip_list)
    # return color_name_list,color_chip_list
    return color_dict
def getTitleImagesFromJSON(item):
    uniqlo_product_title_images_json = item.TitleImagesJSON
    uniqlo_product_title_image_dict = json.loads(uniqlo_product_title_images_json)
    uniqlo_product_title_image_list = []
    for key, value in uniqlo_product_title_image_dict.items():
        for val in value:
            uniqlo_product_title_image_list.append(val)
    
    return uniqlo_product_title_image_list


def sellerApplyProcess(request):

    page_title = ('二手衣上架申請')
    active_tab = 'application'
    template_name_source = 'oscar/customer/application/application_page.html'
    template_name_forward = 'oscar/customer/application/application_page_more_info.html'
    itemexist = True #預設值是true
    message = ''
    sellerID = request.user
    uniqlo_title= ''
    uniqlo_product_img_url =''
    times = '1'
        
    uniqlo_id = request.POST['itemID']
    
    print('post',request.POST['sellerID'],'輸入了商品序號',request.POST['itemID'])

    item = models.UNIQLOItem.objects.get(UNIQLOID=uniqlo_id)
    uniqlo_title = item.UNIQLOTitle
    uniqlo_title_imgs_url_list = getTitleImagesFromJSON(item)
    
    if item != None:
        color_dict = getColorsFromJSON(item)
        # print(color_name_list)
        # print(color_chip_list)

        return render(request, template_name_forward, locals())
    else:
        itemexist = False
        message = '此商品不存在! 請確認是否輸入正確的商品序號!'
        print(message)
        return render(request, template_name_source, locals())

def sellerApplyProcessInfo(request):
    #todo 處理收集到的資料 並且save進records裡面
    print('色碼',request.POST['color_radio_btn'])
    print('用戶',request.POST['sellerID'])
    
    # received_form = forms.SellerApplicationForm(request.POST)
    # if received_form.is_valid():
    #     uniqlo_id =  received_form.cleaned_data['item_id']
    #     try:
    #         item = models.UNIQLOItem.objects.get(UNIQLOID=uniqlo_id)
    #         print(item)
    #         itemexist = True
    #             ## 要寫入的資料
    #         username = request.user
    #         status = '申請已提交，但平台尚未收到賣家寄來的商品'
    #         UNIQLOID=uniqlo_id
    #         size=received_form.cleaned_data['size']
    #         color=received_form.cleaned_data['color']
    #         wishing_price=received_form.cleaned_data['wishing_price']
    #         message =  '成功提交申請!'
    #         title = item.UNIQLOTitle
    #         quantity = received_form.cleaned_data['quantity']
    #         record = models.Application_Records(username=username, status=status, UNIQLOID=uniqlo_id, title = title,
    #                                             size=size, color=color, wishing_price=wishing_price,quantity = quantity)
    #         record.save()
    #         print(username,'成功提交申請!')
    #     except:
    #         itemexist = False
    #         message = '商品序號有誤！請確認是否輸入正確的商品序號！'
    #         username = request.user
    #         print(username,'輸入的商品序號有誤！請確認是否輸入正確的商品序號')

    # print(uniqlo_id)          
    return render(request, 'oscar/customer/application/application_page_more_info.html', locals())

def sellerApplyRecords(request):
    #todo-可查尋 可修改 可刪除
    template_name = 'oscar/customer/application/records.html'
    page_title = ('上架申請查詢')
    active_tab = 'application-records'
    all_records = models.Application_Records.objects.filter(username=request.user)
    recordslist = []

    for value in all_records:
        recordslist.append(value)
    return render(request, template_name, locals())











def collectInfo(request):
    UQItems = models.UNIQLOItem.objects.all()
    UQItem_list = list()
    for _, UQItem in enumerate(UQItems):
        UQItem_list.append("{}".format(str(UQItem) + "<br>"))

    serialNumnCollector = SerialNumberCollector()
    serialset = serialNumnCollector.findOuter()
    print('已完成全部serialNumber的爬蟲')
    for n in serialset:
        if len(n) <= 4:
            continue
        else:
            goodsInfoCollector = GoodsInfoCollector(n)
            isError = goodsInfoCollector.search()

    # goodsInfoCollector = GoodsInfoCollector('433245')
    # goodsInfoCollector.search()
    return render(request, '', locals())
# 爬蟲
class GoodsInfoCollector:
    def __init__(self, serialNumber):
        # 商品序號
        self.serialNumber = serialNumber

        print('現在要找的是'+serialNumber)
        self.colorDict = {}
        # 資料庫需要的資料
        self.typeDict = {('外套類-休閒外套', 'outer-casual-outer'),
                         ('MEN⁄休閒外套', 'outer-casual-outer'),
                         ('外套類-風衣/大衣/西裝外套', 'outer-jacket'),
                         ('風衣大衣西裝外套', 'outer-jacket'),
                         ('外套類-特級極輕羽絨服', 'outer-ultralightdown'),
                         ('外套類-羽絨外套', 'outer-down'),
                         ('外套類-fleece', 'outer-fleece'),
                         ('下身類-休閒長褲', 'bottoms-long-pants'),
                         ('彈性長褲‧休閒長褲', 'bottoms-long-pants'),
                         ('下身類-牛仔褲', 'bottoms-jeans'),
                         ('下身類-休閒長褲', 'bottoms-long-pants'),
                         ('下身類-九分褲・七分褲', 'bottoms-easy-and-gaucho'),
                         ('下身類-緊身褲/內搭褲', 'bottoms-leggings'),
                         ('緊身褲', 'bottoms-leggings'),
                         ('下身類-寬褲', 'bottoms-widepants'),
                         ('下身類-裙子', 'bottom-skirt'),
                         ('下身類-短褲', 'bottoms-short-and-half-pants'),
                         ('上衣類-短袖/背心', 'tops-short-sleeves-and-tank-top'),
                         ('短袖‧背心', 'tops-short-sleeves-and-tank-top'),
                         ('上衣類-長袖‧七分袖', 'tops-short-long-and-3-4sleeves-and-cardigan'),
                         ('MEN⁄T恤(長袖・七分袖)',
                          'tops-short-long-and-3-4sleeves-and-cardigan'),
                         ('MEN⁄T恤(短袖)', 'tops-short-long-and-3-4sleeves-and-cardigan'),
                         ('T恤(長袖・七分袖)', 'tops-short-long-and-3-4sleeves-and-cardigan'),
                         ('設計上衣・襯衫', 'tops-shirts-and-blouses'),
                         ('上衣類-休閒/連帽上衣‧連帽外套', 'tops-sweat-collection'),
                         ('休閒系列‧連帽外套', 'tops-sweat-collection'),
                         ('上衣類-法蘭絨系列', 'tops-flannel'),
                         ('上衣類-針織衫‧開襟外套', 'tops-knit'),
                         ('洋裝‧連身褲', 'tops-dresses'),
                         }

        self.title = ''
        self.type = ''
        self.colorListJSON = ''
        self.titleImages = ''
        self.subImages = ''
        self.description = ''
        self.sizeTable = ''
        self.price = ''

        # 設定selenium
        Chrome_driver_path = 'C:/CodingProject/PythonProject/chromedriver/chromedriver.exe'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(
            'User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"')
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(
            executable_path=Chrome_driver_path, chrome_options=chrome_options)
        # driver.maximize_window()  # 最大化視窗

    def search(self):

        num_exists = models.UNIQLOItem.objects.filter(
            UNIQLOID=self.serialNumber)
        if num_exists.exists():
            print(self.serialNumber, self.title, '已经存在，不需要進行爬蟲')
            return 'ERROR'
        else:
            goodspage = 'https://www.uniqlo.com/tw/store/goods/'+self.serialNumber

        try:
            self.driver.get(goodspage)
            self.goodssoup = BeautifulSoup(
                self.driver.page_source, "html.parser")
            self.driver.close()
        except:
            self.goodssoup = ''

        if self.goodssoup != '':
            print('目前正在搜尋', 'https://www.uniqlo.com/tw/store/goods/'+self.serialNumber)
            self.title = self.getTitle()
            # print('品名', self.title)
            self.type = self.getType()
            # print('種類', self.type)
            self.colorlistJSON = self.getColorList()
            # print('顏色列表', self.colorlistJSON)
            self.titleImages = self.getTitleImages()
            # print('首圖', self.titleImages)
            self.subImages = self.getSubImages()
            # print('附圖', self.subImages)
            self.description = self.getDescription()
            # print('商品描述', self.description)
            self.price = self.getPrice()
            # print('價格', self.price)
            self.save()
            # print('儲存!')
        else:
            print('找不到', 'https://www.uniqlo.com/tw/store/goods/'+self.serialNumber)
            return 'ERROR'

    def getTitle(self):

        result = self.goodssoup.find_all('h1', id='goodsNmArea')
        titleArray = []
        tmpStr = ''
        title = ''
        for g in result:
            tmpStr = g.text
            tmpStr = tmpStr.replace('女裝', '')
            titleArray = tmpStr.split(' ')
            for g in titleArray:
                title += g
        return title

    def getColorList(self):
        # 色塊圖片網址 https://im.uniqlo.com/images/tw/uq/pc/goods/433791/chip/50_433791.gif
        result = self.goodssoup.find_all('ul', id='listChipColor')
        for g in result:
            soup = g.find_all('img')
            for s in soup:
                tmp = str(s)
                tmp = tmp.replace('<img alt="', '')
                tmp = tmp.replace('" height="22" src="', '')
                tmp = tmp.replace(
                    'https://im.uniqlo.com/images/tw/uq/pc/goods/'+self.serialNumber + '/chip/', '')
                tmp = tmp.replace('_'+self.serialNumber +
                                  '.gif" width="22"/>', '')

                colorCode = tmp[-2:]
                color = tmp.replace(colorCode, '')
                self.colorDict[colorCode] = color  # 用來抓首圖
            colorListJSON = json.dumps(
                self.colorDict, indent=4)  # 存進資料庫的資料是JSON
            # print(color, colorCode)
            return colorListJSON

        # print('color?')
        # print(colors)
        # 有顏色 就能抓到首圖

    # 獲取首圖
    def getTitleImages(self):
        tmplist = []
        for color in self.colorDict:
            tmplist.append('https://im.uniqlo.com/images/tw/uq/pc/goods/' +
                           self.serialNumber+'/item/'+color+'_'+self.serialNumber+'.jpg')
        titleimage_dict = {"title image": tmplist}
        titleimageJSON = json.dumps(titleimage_dict, indent=4)
        # print(titleimageJSON)
        return titleimageJSON

    # 獲取附圖#可能為空
    def getSubImages(self):
        result = self.goodssoup.find_all('ul', ['class', 'listimage clearfix'])
        tmp = ''
        unnecessarywords = '''<img '="" alt="商品照片" class="select" height="74" src="https://im.uniqlo.com/images/tw/uq/pc/img/l4/img_listimage_selected.gif" width="74"/>'''
        imagesArray = []
        for g in result:
            # 找到有img的內容
            imgs = g.find_all('img')
            # 針對每個img做處理
            for img in imgs:
                tmp = str(img)
                if tmp == unnecessarywords:
                    continue
                else:
                    # 把不需要的字除掉
                    tmp = tmp.replace('<img height="68" src="', '')
                    tmp = tmp.replace('" width="68"/>', '')
                    tmp = tmp.replace('_mini', '')
                    # 將處理好的圖片網址放進陣列中
                    imagesArray.append(tmp)
        image_dict = {"subimage": imagesArray}
        imageJSON = json.dumps(image_dict, indent=4)
        # print(imageJSON)
        return imageJSON

    def getDescription(self):
        result = self.goodssoup.find_all('p', id='shortComment')
        for g in result:
            tmp = str(g)
            tmp = tmp.replace(
                '<p class="readmore-js-section readmore-js-collapsed" id="shortComment" style="height: 99px;">', '')
            tmp = tmp.replace(
                '<p id="shortComment" style="display: none;"></p>', '')
            # print(tmp)
            return tmp

    # 獲得衣服種類(上衣、褲子、外套...)
    def getType(self):
        clothType = self.goodssoup.find_all('p', ['class', 'pathdetail'], 'a')
        clothTypeArray = []
        clothTypeStr = ""
        tmpStr = ""
        for g in clothType:
            tmpStr = g.text
            tmpStr = tmpStr.replace('\t', '')
            tmpStr = tmpStr.replace('\xa0', '')
            tmpStr = tmpStr.replace('/', '')
            clothTypeStr = tmpStr.replace('\n', '')
            clothTypeStr = clothTypeStr.replace('WOMEN⁄', '')
            clothTypeArray = clothTypeStr.split(" ")
        # print(clothTypeArray[0])

        # self.typeDict = {('outer-casual-outer', '外套類-休閒外套'),
        #                  ('outer-jacket', '外套類-風衣/大衣/西裝外套'),
        #                  ('outer-ultralightdown', '外套類-特級極輕羽絨服'),
        #                  ('outer-down', '外套類-羽絨外套'),
        #                  ('outer-fleece', '外套類-fleece'),
        #                  ('bottoms-long-pants', '下身類-休閒長褲'),
        #                  ('bottoms-jeans', '下身類-牛仔褲'),
        #                  ('bottoms-long-pants', '下身類-休閒長褲'),
        #                  ('bottoms-easy-and-gaucho', '下身類-九分褲 ‧七分褲'),
        #                  ('bottoms-leggings', '下身類-緊身褲/內搭褲'),
        #                  ('bottoms-widepants', '下身類-寬褲'),
        #                  ('bottom-skirt', '下身類-裙子'),
        #                  ('bottoms-short-and-half-pants', '下身類-短褲'),
        #                  ('tops-short-sleeves-and-tank-top', '上衣類-短袖/背心'),
        #                  ('tops-short-long-and-3-4sleeves-and-cardigan', '上衣類-長袖‧七分袖'),
        #                  ('tops-shirts-and-blouses', '上衣類-設計上衣‧襯衫'),
        #                  ('tops-sweat-collection', '上衣類-休閒/連帽上衣‧連帽外套'),
        #                  ('tops-flannel', '上衣類-法蘭絨系列'),
        #                  ('tops-knit', '上衣類-針織衫‧開襟外套'),
        #                  ('tops-dresses', '上衣類-洋裝‧連身褲')}
        for k, v in self.typeDict:
            if clothTypeArray[0] in k:
                print('k:', k, ': ', self.serialNumber,
                      '的種類是', clothTypeArray[0], '順利分類!')
                return v
        print(self.serialNumber, '找不到適合的分類耶...', '我只知道他是', clothTypeArray[0])
        return 'default'

        # return clothTypeArray[0]

    def getPrice(self):
        price = self.goodssoup.find_all('li', id='price')
        tmpStr = ''
        for g in price:
            tmpStr = g.text
            tmpStr = tmpStr.replace('<li class="price" id="price">', '')
            tmpStr = tmpStr.replace('NT$', '')
            tmpStr = tmpStr.replace('<span class="tax"></span></li>', '')
            tmpStr = tmpStr.replace('\xa0', '')
            tmpStr = tmpStr.replace(',', '')

        # print(price)
        return int(tmpStr)

    # 將爬到的資料寫進資料庫
    def save(self):

        order_exists = models.UNIQLOItem.objects.filter(
            UNIQLOID=self.serialNumber)
        if order_exists.exists():
            print(self.serialNumber, self.title, '已经存在')
            # ，现在更新数据，更新的数据id：',order_exists.last().id)
        else:

            unit = models.UNIQLOItem.objects.create(
                UNIQLOID=self.serialNumber,
                UNIQLOTitle=self.title,
                OriginalPrice=self.price,
                ClothesColorJSON=self.colorlistJSON,
                TitleImagesJSON=self.titleImages,
                SubImagesJSON=self.subImages,
                ClothesType=self.type,
                Description=self.description
            )
            print('順利儲存!')
            unit.save()  # 寫入資料庫

class SerialNumberCollector:
    def __init__(self):

        # 設定selenium
        Chrome_driver_path = 'C:/CodingProject/PythonProject/chromedriver/chromedriver.exe'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(
            'User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"')
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')         
        self.driver = webdriver.Chrome(
            executable_path=Chrome_driver_path, chrome_options=chrome_options)
        # driver.maximize_window()  # 最大化視窗

    def getSoup(self, suffix):
        page = 'https://www.uniqlo.com/tw/store/feature/women/'+suffix
        self.driver.get(page)
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        return soup

    # casual-outer
    def findOuter(self):
        # 用來爬全網站的網址suffix
        catagory = ['outer/casual-outer/',
                    'outer/jacket/', 'outer/ultralightdown/', 'outer/down', 'outer/fleece',
                    'bottoms/jeans/', 'bottoms/long-pants/', 'bottoms/easy-and-gaucho/', 'bottoms/leggings/', 'bottoms/widepants/',
                    'bottoms/short-and-half-pants/', 'bottom/skirt',
                    'tops/short-sleeves-and-tank-top/', 'tops/long-and-3-4sleeves-and-cardigan/', 'tops/shirts-and-blouses',
                    'tops/sweat-collection', 'tops/flannel', 'tops/knit', 'tops/dresses']
        serialset = set()
        serialnum = ''
        for item in catagory:
            print(item)
            serialnum = ''
            result = self.getSoup(item)
            result = result.find_all(
                'dt', ['class', 'name'])
            for g in result:
                tmp = str(g)
                tmp = tmp.replace(
                    '<a href="https://www.uniqlo.com/tw/store/goods/', '')
                tmp = tmp.replace('<dt class="name">', '')
                for c in tmp:
                    try:
                        int(c)
                        serialnum += c
                    except:
                        serialnum += '/'
                        continue
            num = serialnum.split('/')

            for i in range(num.count('')):
                num.remove('')

            print(num)
            for n in num:
                serialset.add(n)

        return serialset
