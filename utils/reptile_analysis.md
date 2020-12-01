# 百度图库爬虫分析

baseurl : https://image.baidu.com/

### 测试：不同的搜索命令

search : 折线图
```
url : https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1606436330409_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E6%8A%98%E7%BA%BF%E5%9B%BE
翻页查询 url : https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11315969543439149654&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%8A%98%E7%BA%BF%E5%9B%BE&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E6%8A%98%E7%BA%BF%E5%9B%BE&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&gsm=1e&1606435955942=
```

search : 柱状图
```
url : https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1606435805984_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E6%9F%B1%E7%8A%B6%E5%9B%BE
翻页查询 url : https://image.baidu.com/search/acjson?tn=resultjson_com&logid=10495703989160200894&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%9F%B1%E7%8A%B6%E5%9B%BE&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E6%9F%B1%E7%8A%B6%E5%9B%BE&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&gsm=1e&1606435886480=
```
    
    
### 信息提取：解析GET数据

url : base : https://image.baidu.com/search/index

- tn=baiduimage，所使用的分区/功能
- ct=201326592，引发查询数据的改变，推测可能与地域、记录、个性推荐等有关，可以忽略
- ipn=r，推测 r 为 result 缩写
- fm=result，推测为 format 缩写
- fmq=1606435805984_R  /  1606435805984_R：可能为查询结果记录，不影响查询结果
- word=%E6%9F%B1%E7%8A%B6%E5%9B%BE  /  %E6%9F%B1%E7%8A%B6%E5%9B%BE


翻页查询 url : base : https://image.baidu.com/search/acjson
- tn=resultjson_com，所使用的分区/功能
- logid=10495703989160200894，引发查询数据的改变，可能为记录相关；在同一次检索的不同翻页查询中
没有变化，可以在每次爬虫前获取一次
- ipn=rj，推测 rj 为 result_json 缩写
- ct=201326592，同 url 中所示
- fp=result，推测与 url 中 fm 类似
- queryWord=%E6%9F%B1%E7%8A%B6%E5%9B%BE
- word=%E6%9F%B1%E7%8A%B6%E5%9B%BE
- pn=30，开始展示的id
- rn=30，展示的数量

### json解析
查询 https://image.baidu.com/search/acjson?tn=resultjson_com&logid=10116278434388387296&ipn=rj&queryWord=%E6%8A%98%E7%BA%BF%E5%9B%BE&word=%E6%8A%98%E7%BA%BF%E5%9B%BE&pn=0&rn=1 ，可以解析出以下json文件：

```json
{
    "queryEnc":"%D5%DB%CF%DF%CD%BC",
    "queryExt":"折线图",
    "listNum":1948,
    "displayNum":116812,
    "gsm":"1",
    "bdFmtDispNum":"约116,000",
    "bdSearchTime":"",
    "isNeedAsyncRequest":0,
    "bdIsClustered":"1",
    "data":[
        {
            "adType":"0",
            "hasAspData":"0",
            "thumbURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1202112146,122929379&fm=26&gp=0.jpg",
            "middleURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1202112146,122929379&fm=26&gp=0.jpg",
            "largeTnImageUrl":"",
            "hasLarge":0,
            "hoverURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1202112146,122929379&fm=26&gp=0.jpg",
            "pageNum":0,
            "objURL":"ippr_z2C$qAzdH3FAzdH3Fckalbbjclcddc_z&e3Bv1g_z&e3Bf5i7vf_z&e3Bv54AzdH3Ft4w2jfAzdH3Fda8ba8d0AzdH3Fuv1kjbn0ulnj9ajlww9jjkwudww8ajv1_z&e3B3rj2",
            "fromURL":"ippr_z2C$qAzdH3FAzdH3F4p_z&e3Bf5i7_z&e3Bv54AzdH3Fk7ftgjffAzdH3F1da8ba8d0AzdH3Fd8lnm8aa9_0cndnd_z&e3Bfip4s",
            "fromURLHost":"mt.sohu.com",
            "currentIndex":"",
            "width":998,
            "height":554,
            "type":"jpeg",
            "is_gif":0,
            "isCopyright":0,
            "resourceInfo":null,
            "strategyAssessment":"3178238610_26_0_0",
            "filesize":"",
            "bdSrcType":"0",
            "di":"209000",
            "pi":"0",
            "is":"0,0",
            "imgCollectionWord":"",
            "replaceUrl":[
                {
                    "ObjURL":"http://img1.imgtn.bdimg.com/it/u=1202112146,122929379&fm=214&gp=0.jpg",
                    "ObjUrl":"http://img1.imgtn.bdimg.com/it/u=1202112146,122929379&fm=214&gp=0.jpg",
                    "FromURL":"http://mt.sohu.com/business/d20180127/219361004_753232.shtml",
                    "FromUrl":"http://mt.sohu.com/business/d20180127/219361004_753232.shtml"
                }
            ],
            "hasThumbData":"0",
            "bdSetImgNum":0,
            "partnerId":0,
            "spn":0,
            "bdImgnewsDate":"2018-01-27 22:20",
            "fromPageTitle":"图14 员工离职率对比折线图</strong>",
            "fromPageTitleEnc":"图14 员工离职率对比折线图",
            "bdSourceName":"",
            "bdFromPageTitlePrefix":"",
            "isAspDianjing":0,
            "token":"",
            "imgType":"",
            "cs":"1202112146,122929379",
            "os":"2982448758,3486580812",
            "simid":"3101160970,3762890250",
            "personalized":"0",
            "simid_info":null,
            "face_info":null,
            "xiangshi_info":null,
            "adPicId":"0",
            "source_type":""
        },
        {

        }
    ]
}
```

可以发现，有用的图片url处于 data[i].thumburl 中

### 爬虫

由上，可以组织爬虫查询：https://image.baidu.com/search/acjson，data为：
```json
{
  "tn":"resultjson_com", 
  "logid":"10116278434388387296",
  "ipn":"rj",
  "queryWord":"XXX", 
  "word":"XXX",
  "pn":"a",
  "rn":"b"
}
```
- logid : 每次爬虫前检索得到logid
- pn : 开始的id
- rn : 获取的数量


从获取的json文件中，检索 data[i].thumburl 的数据，即为url




# bing图库爬虫分析

baseurl : https://cn.bing.com/images/

### 测试：不同的搜索命令

search : 折线图
```
url : https://cn.bing.com/images/search?q=%E6%8A%98%E7%BA%BF%E5%9B%BE&qs=n&form=QBIR&sp=-1&pq=zhe%27xian%27tu&sc=0-11&cvid=22B7C12838CD4C46997042F2F5788472&first=1&tsc=ImageBasicHover&scenario=ImageBasicHover
翻页查询 url : https://cn.bing.com/images/async?q=折线图&first=37&count=35&relp=35&tsc=ImageBasicHover&scenario=ImageBasicHover&datsrc=I&layout=RowBased_Landscape&mmasync=1&dgState=x*276_y*1152_h*183_c*1_i*36_r*7&IG=4433E43AAAAE479EBB75F85D5680944E&SFX=2&iid=images.5538
```

search : 柱状图
```
url : https://cn.bing.com/images/search?q=%E6%9F%B1%E7%8A%B6%E5%9B%BE&qs=n&form=QBIR&sp=-1&pq=%E6%9F%B1%E7%8A%B6%E5%9B%BE&sc=8-3&cvid=4BF98C1265124F5680F0C23B0AE65592&first=1&tsc=ImageBasicHover&scenario=ImageBasicHover
翻页查询 url : https://cn.bing.com/images/async?q=%e6%9f%b1%e7%8a%b6%e5%9b%be&first=40&count=35&relp=35&tsc=ImageBasicHover&scenario=ImageBasicHover&datsrc=I&layout=RowBased_Landscape&mmasync=1&dgState=x*0_y*0_h*0_c*6_i*36_r*6&IG=5F65C2F3D94C49138A5EA7FF88BF3962&SFX=2&iid=images.5540
```
    
### 信息提取：解析GET数据

url : base : https://cn.bing.com/images/search

- q=%E6%8A%98%E7%BA%BF%E5%9B%BE，为 query 简写
- pq=zhe%27xian%27tu，与 q 一致
- sc=0-11
- cvid=22B7C12838CD4C46997042F2F5788472
- first=1


翻页查询 url : base : https://cn.bing.com/images/async
- q=%e6%9f%b1%e7%8a%b6%e5%9b%be，为 query 简写
- qft=+filterui:color2-FGcls_WHITE+filterui:imagesize-custom_512_512，筛选白色、512X512以上
- first=37，开始id
- count=35，数量
- relp=35，未发现明显作用，可以忽略
- mmasync=1，可能为async的固定参数，不可改变，否则加载出错

### html解析
查询 https://cn.bing.com/images/async?q=%E6%8A%98%E7%BA%BF%E5%9B%BE&first=0&count=1&mmasync=1 ，可以解析出以下html文件（主体部分）：

```html
{
<div class="dg_b" role="main" data-pagewidth="0" data-clientwidth="0" data-disableRefreshOnIFrame="1"
     data-reloadableInIframe="">
    <div id="mmComponent_images_1" class="dgControl hover" style="width:1516px"
         data-nextUrl="/images/async?q=%e6%8a%98%e7%ba%bf%e5%9b%be&amp;first=2&amp;count=35&amp;relp=1&amp;tsc=ImageBasicHover&amp;scenario=ImageBasicHover&amp;datsrc=I&amp;layout=RowBased&amp;mmasync=1&amp;dgState=x*244_y*0_h*200_c*1_i*2_r*1"
         data-postData="" data-iid="images.5056" data-layout="row">
        <ul data-row=0 class="dgControl_list " data-infullrow=1 style="">
            <li data-idx=1 style="width:232px; height: 200px">
                <div class="iuscp varh" style="width:232px" data-hovstyle="" data-evt="1">
                    <div class="imgpt"><a class="iusc" style="height:200px;width:232px"
                                          m="{&quot;cid&quot;:&quot;qTwEnan4&quot;,&quot;purl&quot;:&quot;https://wenwen.sogou.com/z/q825286701.htm&quot;,&quot;murl&quot;:&quot;https://pic.wenwen.soso.com/pqpic/wenwenpic/0/20200905072601-1377158880_png_3442_2972_201696/0&quot;,&quot;turl&quot;:&quot;https://tse1-mm.cn.bing.net/th?id=OIP.qTwEnan4GiMdiu0jeB7ZLgHaGZ&amp;pid=15.1&quot;,&quot;md5&quot;:&quot;a93c049da9f81a231d8aed23781ed92e&quot;,&quot;shkey&quot;:&quot;e8ko6ZaWblCEc770d5UTMO/gNEoaPEl2Gcja7ON0m4U=&quot;,&quot;t&quot;:&quot;用wps怎么画这样的折线图&quot;,&quot;mid&quot;:&quot;8FDC2B382A5FDB5C6325DEB63A4482E9C3A11F56&quot;,&quot;desc&quot;:&quot;&quot;}"
                                          onclick="sj_evt.fire('IFrame.Navigate', this.href); return false;"
                                          href="/images/search?view=detailV2&amp;ccid=qTwEnan4&amp;id=8FDC2B382A5FDB5C6325DEB63A4482E9C3A11F56&amp;thid=OIP.qTwEnan4GiMdiu0jeB7ZLgHaGZ&amp;mediaurl=https%3a%2f%2fpic.wenwen.soso.com%2fpqpic%2fwenwenpic%2f0%2f20200905072601-1377158880_png_3442_2972_201696%2f0&amp;exph=2972&amp;expw=3442&amp;q=%e6%8a%98%e7%ba%bf%e5%9b%be&amp;simid=607994282390588004&amp;ck=4279D813B29153BB4F17C38438164597&amp;selectedIndex=0&amp;FORM=IRPRST"
                                          h="ID=images,5025.1">
                        <div class="img_cont hoff"><img class="mimg" style="background-color:#465159;color:#465159"
                                                        height="200" width="232"
                                                        src="https://tse3-mm.cn.bing.net/th/id/OIP.qTwEnan4GiMdiu0jeB7ZLgHaGZ?w=232&amp;h=200&amp;c=7&amp;o=5&amp;dpr=1.25&amp;pid=1.7"
                                                        alt="折线图 的图像结果"/></div>
                    </a>
                        <div class="img_info hon"><span class="nowrap">3442 x 2972 &#183; png</span>
                            <div class="lnkw"><a title="wenwen.sogou.com" target="_blank"
                                                 href="https://wenwen.sogou.com/z/q825286701.htm" h="ID=images,5053.1">wenwen.sogou.com</a>
                            </div>
                        </div>
                    </div>
                </div>
            </li>
        </ul>
        <div id="mmComponent_images_1_exp"
             class="expandButton txtaft " data-astates="" data-expandOn=" scroll" data-expClkToScr="0" data-expScrKey=""
             data-disScrLog="" data-exptiming=""><span class="expInner"><a href="javascript:void(0);" title="展开"
                                                                           role="button"></a></span></div>
    </div>
    <div id="bop_container" class="invis" data-chkfstpg="1">
        <div id="bop_announce" class="b_hide" tabindex="-1" title="新图像已加载"></div>
    </div>
</div>
}
```

可以发现，有用的图片url处于 a @class="iusc" @href 中，形如 : /images/search?view=detailV2&amp;ccid=qTwEnan4&amp;id=8FDC2B382A5FDB5C6325DEB63A4482E9C3A11F56&amp;thid=OIP.qTwEnan4GiMdiu0jeB7ZLgHaGZ&amp;mediaurl=https%3a%2f%2fpic.wenwen.soso.com%2fpqpic%2fwenwenpic%2f0%2f20200905072601-1377158880_png_3442_2972_201696%2f0&amp;exph=2972&amp;expw=3442&amp;q=%e6%8a%98%e7%ba%bf%e5%9b%be&amp;simid=607994282390588004&amp;ck=4279D813B29153BB4F17C38438164597&amp;selectedIndex=0&amp;FORM=IRPRST


### sub_url 解析

查询 https://cn.bing.com/images/search?view=detailV2&amp;ccid=qTwEnan4&amp;id=8FDC2B382A5FDB5C6325DEB63A4482E9C3A11F56&amp;thid=OIP.qTwEnan4GiMdiu0jeB7ZLgHaGZ&amp;mediaurl=https%3a%2f%2fpic.wenwen.soso.com%2fpqpic%2fwenwenpic%2f0%2f20200905072601-1377158880_png_3442_2972_201696%2f0&amp;exph=2972&amp;expw=3442&amp;q=%e6%8a%98%e7%ba%bf%e5%9b%be&amp;simid=607994282390588004&amp;ck=4279D813B29153BB4F17C38438164597&amp;selectedIndex=0&amp;FORM=IRPRST

```html
<div class="richImage error">
    <div class="mainContainer">
        <div class="imgContainer"><img
                src="https://tse2-mm.cn.bing.net/th/id/OIP.Ajd_bkesmstRmedlLoYYlAHaF7?pid=Api&amp;rs=1" alt="查看源图像"
                class=" nofocus" tabindex="0" aria-label="查看源图像" data-bm="6"></div>
    </div>
</div>
<div class="mainImgErr"></div>
```

所选图片原图的 url 即为div @mainContainer / div @imgContainer / img @ nofocus / @src 下，形如 https://tse2-mm.cn.bing.net/th/id/OIP.Ajd_bkesmstRmedlLoYYlAHaF7?pid=Api&amp;rs=1
此时发现此 url 与上一步中 a/@m 中 "murl" 相同，所以可以直接访问上一步


### 爬虫

由上，可以组织爬虫查询：https://cn.bing.com/images/async，data为：
```json
{
  "q":"XXX", 
  "first":"a",
  "count":"b",
  "mmasync":"1",
  "qft": "+xx+xx"
}
```

从获取的html文件中，检索 a @class="iusc" @m， 这个json数组中 "murl" 一项为图片地址