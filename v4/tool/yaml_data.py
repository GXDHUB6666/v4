import os
import yaml

class Yaml_until:

    def yaml_read(self):
        with open('../data/login.yml','r',encoding="UTF-8") as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value

    def yaml_write(self,data):
        with open('../data/login.yml','w',encoding="UTF-8") as f:
            yaml.dump(stream=f,data=data,allow_unicode=True)

    def yaml_clean(self):
        with open('../data/login.yml', 'w', encoding="UTF-8") as f:
            f.truncate()

    def data(self):
        datas = []
        for data in self.yaml_read():
            datas.append((data.get('username'),
                          data.get('pwd'),
                          data.get('expect'),
                          data.get('success'))
                         )
        return datas

if __name__ == '__main__':
    print(os.getcwd()+'../data/login.yml')