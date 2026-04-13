import os as o
from pathlib import Path
import urllib.request as ur
import urllib.error as ue
import subprocess as s
import json as j
import logging as l
import shutil as st
import mimetypes as m
import sys as ss
class PathD :
    def __init__(self,Ghname,Repon,j_name,pf_name) :
        m.init()
        self.Gh_url = f'https://raw.githubusercontent.com{Ghname}/{Repon}/HEAD'
        self.Base_Dih = Path(__file__).parent.absolute()
        self.j_name = j_name
        self.pf_name = pf_name
        self.run()
    def don_nha(self) :
        main_dir = Path(__file__).resolve()
        folder_goc = main_dir.parent
        folder_file = folder_goc/self.pf_name
        folder_file.mkdir(exist_ok = True)
        new_path = folder_file/main_dir.name
        if main_dir != new_path :
            st.move(str(main_dir),str(new_path))
        o.chdir(folder_file)
        self.Base_Dih = folder_file
        List_folder = ['Code','Asset']
        for folder in List_folder :
            (Path(folder)).mkdir(exist_ok = True)
    def Code_log(self) :
        self.log = self.Base_Dih/'Asset'/'log.txt'
        l.basicConfig(                                                           level = l.INFO,                                                   format = '%(asctime)s -%(levelname)s - %(message)s',                                     handlers =  [                                                              l.FileHandler(self.log,encoding = 'utf-8'),                                                                   l.StreamHandler()                                   ]                                                                    )
        self.log = l.getLogger('Github PathD Model 1')
        self.log.info('-'* 30 +'Chao mung bozo cua toi tro lai co le la mot lan nua' + '-' * 30)
    def Djson (self) :
        if not self.j_name.endswith('.json') :
            self.j_name += '.json'
        path_j = self.Base_Dih/'asset'/self.j_name
        if path_j.exist() :
            self.log.info(f'umm,file {self.j_name} co san roi a...ngon,check luon :3')
            with open(path_j,'r',encoding = 'utf-8') as f :
                return j.load(f)
        url_j = f'{self.Gh_url}/{self.j_name}'
        try :
            with ur.urlopen(url_j) as dopixi :
                data_1 = dopixi.read().decode('utf-8')
                config = j.loads(data_1)
                with open(path_j, 'w',encoding = 'utf-8') as f :
                    j.dump(config,f,indent = 4,ensure_ascii = False)
                    self.log.info(f'Toi nhot file {self.j_name} vao nha roi...yen tam vao nha di,chau no khong can dau(dop thi khong chac)')
                return config
        except ue.HTTPError as e :
            self.log.error(f'umm,file {self.j_name} o dau ay nhi... chet mia,bo bi mu roi,bo eo tim thay file,huhu :( [ bug :{e.code} ]')
            return False
        except ue.URLError as e :
            self.log.error(f'umm,nay bozo,toi nghi cuc wifi nha ban om phan lao a bien roi...that long ma noi,toi khuyen ban nen nhin lai cuc wifi hoac url di,dung de bon no tao phan (idk, ly do : {e.reason})')
            return False
        except JSONdecodeError as e :
            self.log.error(f'xem lai file json di,toi nghi hoi co ty van de o day do...(bug is {e})')
            return False
        except Exception as e :
            self.log.error(f'fix bug plss,bug is {e}')
            return False
    def chuyen_nha(self,fn) :
        mime_type,_ = m.guess_type(fn)
        is_code = False
        if mime_type :
            if mime_type.startswith('text') or 'json' in mime_type or 'javascirpt' in mine_type :
                is_code = True
        sub_folder = 'Code' if is_code else 'Asset'
        save_path = self.Base_Dih/ sub_folder/fn
        return save_path
    def Dlib(self,lib_name) :
        try :
            self.log.info(f'ok,doi ty...dang cai liblary :3')
            __import__ (lib_name)
            self.log.info(f'u,ngon,thu vien tai san roi...')
        except ImportError :
            try :
                self.log.info(f'ua,chua cai pip a,ok doi them chut...')
                s.check_call([ss.executable,'-m','pip','install',lib_name])
                self.log.info('ok,on roi day :3')
            except Exception as e :
                self.log.info(f'fix bug plsss,bug is {e}')
        except Exception as e :
            self.log.info(f'fix bug plss,bug is {e}')
    def Dfile(self) :
        Config_file = self.Djson()
        if not Config_file :
            return
        if 'liblary' in Config_file and isinstance(Config_file['liblary'],list) :
            for lib in nahh['liblary'] :
                self.Dlib(lib)
        List_MFile = ['Code','Asset']
        for model_file in List_MFile :
            if model_file in Config_file and isinstance(Config_file[model_file],dict) :
                for g_name,info in Config_file[model_file].items() :
                    re_name = info.get('file_name',g_name)
                    ver = info.get('ver','0.0')
                    Spath = self.chuyen_nha(re_name)
                    new_urlf = f'{self.Gh_url}/{g_name}'
                    try :
                        self.log.info(f'ok,tim duoc file {g_name} roi,gio thi tai roi di ngu thoi bozo :3 ( ver : {ver})')
                        with urlopen(new_urlf) as h :
                            data = h.read()
                            with open(Spath,'wb') as f :
                                f.write(data)
                                self.log.info(f'ngon,tai xong file {g_name} roi <3')
                    except Exception as e :
                        self.log.info(f'fix bug plss,bug is {e}')
    def run(self) :
        self.don_nha()
        self.Code_log()
        self.Dfile()
