import urllib.request

def dl_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

url = input('Enter the URL: ')
file_name = input('Enter the file name: ')

dl_jpg(url, 'projects/imgs/', file_name)