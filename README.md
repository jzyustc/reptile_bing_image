# Async Reptile Bing Images

We can use this package to reptile images from Bing asynchronously.

This package has features as following:

- asynchronous reptile : we use aiohttp to download images asynchronously.

  - we use basic methods that prevent the server from ban our IP
   
- config file : we need to write a config file to provide parameters for the functions.

- log mode : we apply a log module to log the info and error, so as to better support async.


### Reptile

To get images in bing engine, we need two steps :

1. Search the query word, and get image urls from the html response

    Then store them in a file (split by some chars), to make it easier to use later

2. Download each image by url, and store in a folder


### Quick Start

You can quickly use this package by following steps:

1. First you should direct to `https://cn.bing.com/images/async?q=query_word&first=start_id&count=number&mmasync=1`
    in your browser
    - replace **query_word** with the key word you want to search
    - replace **start_id** with the start id of all searched images
    - replace **number** with the number of searched image in this request
    
    Just try to request many time, varying **start_id** from 0 to k***number**, and stop until you find that between two
    request the results are the same. 
    
    Then you know how many images can you get by this query condition
    
    - in the future version , we will try to replace this step with a function (to auto-detect the number of images that
    we can get in a query condition), but now you have to do this manually :(
     
2. create a folder under at the same path, and then create a file named "reptile_bing.conf".

    As an example, we create "example/reptile_bing.conf" here.
    
    You can copy almost all of the content in "example/reptile_bing.conf" to your "reptile_$engine.conf"

3. in your "reptile_bing.conf", modify these items:

    - make *url_task.query_num * url_task.query.count* a little larger than the number of images 
    you can get by this query condition (obtained from step1)
    
    - modify urls_task.query.q to your query_word
    
4. just program a python file (just like what we do in example.py) to download images!

### Advanced Usage

It just need three steps to use all of functions of this package:

1. Create a folder under at the same path, e.g. "example/"

2. Create a config file under the former folder named "reptile_$engine.conf", 
where $engine means different searching engine (NOTICE that we just support "bing" here, 
but we might add more engines such as baidu and google later), e.g. "example/reptile_bing.conf"

    Then change the content in config file, basic format like below:
    
    Some information of parameters are given in [./utils/reptile_analysic.md](https://github.com/jzyustc/reptile_bing_image/blob/master/utils/reptile_analysis.md)
    
    ```conf
        
    # split char of the image urls (not applied yet)
    split_char = "\n"
    
    # root path of the created folder
    root_path = "example/"
    
    # path to save urls and images (located under rootpath)
    images_urls_filename = "image_urls.txt"
   
    # info log file's name (located under rootpath)
    info_log_filename = "info_log.txt"
   
    # error log file's name (located under rootpath)
    error_log_filename = "error_log.txt"
   
    # path to save images (located under rootpath)
    images_path = "images/"
    
    # task to get urls
    url_task {
    
      # base url of getting image urls
      base_url = "https://cn.bing.com/images/async"
    
      # start id of searching
      start = 0
    
      # number of query
      query_number = 10
    
      # base structure of GET query
      query = {
        q = "YOUR SEARCH"
        first = 0
        count = 300
        mmasync = "1"
        # 白色，至少512X512
        qft = "+filterui:color2-FGcls_WHITE+filterui:imagesize-custom_512_512"
      }
    
      # step of asyn
      asyn_step = 1
    
      # image_size chosen after get urls
      image_size_w_min = 512
      image_size_h_min = 512
    
    }
    
    
    # task to download images
    img_task {
    
      # start id of searching
      start = 0
    
      # number of images, -1 means all imgs
      download_number = -1
    
      # step of asyn
      asyn_step = 50
    
      # allowed_ext
      allowed_ext = [".jpg", ".png", ".gif", ".bmp"]
    
    }
    
    ```
   
   **Notice** :
   
   - you should use the same method as in [./utils/reptile_analysic.md](https://github.com/jzyustc/reptile_bing_image/blob/master/utils/reptile_analysis.md)
        to find how many images can you get by this query word, and set *url_task.query_num * url_task.query.count* 
        a little larger than this number, to prevent from getting 0 image_urls in a request
    

3. Program a python file to use the package, e.g. :

    ```python
   
    from utils.Reptile import Reptile
   
    path = "example/" 
   
    reptile = Reptile(path, "bing")
    reptile.reptile_urls()
    reptile.reptile_imgs()

    ```
    
    
    
### overview

**example.py** is the example of programming a python file to use this package

**example** is the example of create a folder to support reptile

**utils** contains almost all of tools we need to use.

- Log.py : define class ReptileLog to ensure the logging progress.

- Reptile.py : define class Reptile to accomplish the tasks of getting urls and downloading images.

- reptile_utils.py : apply some supporting function, such as get one url, download one image, load config, random ip and so on.


### existing problems:

The package has some bugs and problems to be repaired, and wo list them as below :

1. "split_char" item in config file not applied

2. "image_size_w_min" and "image_size_h_min" items not applied yet

3. Add a function to auto detect number of images we can get in a query condition.

4. to be continue...