import requests, os

tf_ver = os.getenv('TF_VERSION')
url = "https://releases.hashicorp.com/terraform/{ver}/terraform_{ver}_linux_amd64.zip".format(ver = tf_ver)

print("Downloading: {}".format(url))
r = requests.get(url)

filename = url.split('/')[-1]
 
with open(filename,'wb') as output_file:
    output_file.write(r.content)
 
print('Download finished')