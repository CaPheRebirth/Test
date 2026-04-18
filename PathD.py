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
import importlib as il
import importlib.util as iu
ss.dont_write_bytecode = True
class PathD :
    def __init__(self,Ghname,Repon,j_name,pf_name) :
        m.init()
        self.Gh_url = f'https://raw.githubusercontent.com/{Ghname}/{Repon}/HEAD'
        self.Base_Dih = Path(__file__).parent.absolute()
        self.j_name = j_name
        self.pf_name = pf_name
        Asset_path = self.Base_Dih/'Asset'
        Asset_path.mkdir(exist_ok = True)
        self.run()
    def lib_module(self) :
        list_lib = ['pillow']
        self.log.info(f'umm,doi toi tai thu vien can thiet de chay tool cai da')
        for lib in list_lib :
            self.Dlib(lib)
        self.log.info('ok,xong:3')
    def don_nha(self) :
        main_dir = Path(__file__).resolve()
        import __main__
        try :
            if not hasattr(__main__,"__file__") :
                folder_goc = Path("/sdcard/Documents/Pydroid3").resolve()
            else :
                test_dir = Path(__main__.__file__).resolve()
                folder_goc = test_dir.parent 
        except Exception as e :
            self.log.error(f"fix bug plss,bug is {e} (don_nha 1)")
        folder_file = folder_goc/self.pf_name
        Dpathd = folder_file/'__init__.py'
        folder_file.mkdir(exist_ok = True)
        (Dpathd).touch(exist_ok = True)
        list_callf = [main_dir,test_dir,Asset]
        for file in list_callf :
            new_path = folder_file/file.name
            if file.exists() :    
                if file != new_path :
                    st.move(str(file),str(new_path))
            else :
                self.log.info('ngon,do phai don file nua,co san roi,gio di tiep thoi :3')
        o.chdir(folder_file)
        self.Base_Dih = folder_file
        List_folder = ['Code']
        for folder in List_folder :
            (Path(folder)).mkdir(exist_ok = True)
        code_dir = Path("Code")/'__init__.py'
        (code_dir).touch(exist_ok = True)
    def Code_log(self) :
        self.log = self.Base_Dih/'Asset'/'log.txt'
        l.basicConfig(                                                           level = l.INFO,                                                   format = '%(asctime)s -%(levelname)s - %(message)s',                                     handlers =  [                                                              l.FileHandler(self.log,encoding = 'utf-8'),                                                                   l.StreamHandler()                                   ]                                                                    )
        self.log = l.getLogger('Github PathD Model 1')
        self.log.info('-'* 15 +'Chao mung bozo cua toi tro lai co le la mot lan nua' + '-' * 15)
    def Djson (self) :
        if not self.j_name.endswith('.json') :
            self.j_name += '.json'
        path_j = self.Base_Dih/'asset'/self.j_name
        if path_j.exists() :
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
            self.log.error(f'fix bug plss,bug is {e} (Djson)')
            return False
    def chuyen_nha(self,fn) :
        mime_type,_ = m.guess_type(fn)
        is_code = False
        if mime_type :
            if mime_type.startswith('text') or 'json' in mime_type or 'javascirpt' in mime_type :
                is_code = True
        sub_folder = 'Code' if is_code else 'Asset'
        save_path = self.Base_Dih/ sub_folder/fn
        return save_path
    def Dlib(self,lib_name) :
        import __main__
        try :
            self.log.info(f'umm,co san {lib_name} roi a,ngon,import luon :3')
            lib_name = "PIL" if lib_name.lower() == "pillow" else lib_name
            lib = il.import_module(lib_name)
            setattr(__main__,lib_name,lib)
            self.log.info('ok,xong roi day <3')
        except ImportError :
            try :
                self.log.info(f'uhh,chua tai {lib_name} a... thoi duoc doi ty nhe bozo :3')
                s.check_call([ss.executable,'-m','pip','install',lib_name])
                self.log.info('ok,tai xong roi day,gio import thoi :D')
                lib = il.import_module(lib_name)
                setattr(__main__,lib_name,lib)
                self.log.info('ok,on roi day:3')
            except Exception as e :
                self.log.error(f'fix bug plss,bug is {e} (Dlib 1)')
        except Exception as e :
            self.log.error(f'W : fix bug plss,bug is {e} (Dlib 2)')        
    def Dfile(self) :
        Config_file = self.Djson()
        if not Config_file :
            return
        if 'liblary' in Config_file and isinstance(Config_file['liblary'],list) :
            for lib in Config_file['liblary'] :
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
                        with ur.urlopen(new_urlf) as h :
                            data = h.read()
                            with open(Spath,'wb') as f :
                                f.write(data)
                                self.log.info(f'ngon,tai xong file {g_name} roi <3')
                    except Exception as e :
                        self.log.error(f'W : fix bug plss,bug is {e} (Dfile)')
    def Dasset(self) :
        import __main__
        try :
            from PIL import Image
            asset_dih = self.Base_Dih /'Asset'
            for file_asset in asset_dih.glob('*') :
                name_va = file_asset.stem
                m_type,_ = m.guess_type(str(file_asset))
                if m_type and m_type.startswith('image') :
                    try :
                        self.log.info(f'umm,doi toi nhet {file_asset} vao cai da :3')
                        img_ob = Image.open(file_asset)
                        setattr(__main__,name_va,img_ob)
                        self.log.info('ok,da nhet {file_asset} vao main,gio dung di bozo:3')
                    except Exception as e :
                         self.log.warn(f'S : a bozo, {file_asset} co van de ty van de,toi khuyen bro nen xem lai di,thoi toi lam tiep day (bug is  : {e},Dasset line 143 - 149) ')
                         pass
                else :
                    setattr(__main__,name_va,str(file_asset))
                    self.log.info(f'umm,xin loi bozo,file {file_asset} khong phai img nen toi danh gui path vay,mong dai nhan tha mang cho tieu nhan :3 ')
        except Exception as e :
            self.log.error(f'W : fix bug plss,bug is {e} (Dasset)')
    def Dcode(self) :
        import __main__ as _chong_yeu_
        code_path = self.Base_Dih/'Code'
        for C in code_path.glob('*.py') :
            self.log.info(f'umm,doi to nap module ty nhe cau :3(ghi ten de cau de check : {C.stem})')
            if C.name == '__init__.py' : continue
            try :
                mod_name = C.stem
                spec = iu.spec_from_file_localtion()
                emod = iu.module_from_spec(spec)
                spec.loader.exec_module(emod)
                setattr(__main__,mod_name,emod)
                self.log.info(f'ok xong,arigato daisuki :3')
            except Exception as e :
                self.log.error(f'W : fix bug plss,bug is {e} (Dcode)')
    def run(self) :
        self.Code_log()
        self.don_nha()
        self.lib_module()
        self.Dfile()
        self.Dasset()
        self.Dcode()
        self.log.info('om to cai nao,arigato daisuki (⁠つ⁠≧⁠▽⁠≦⁠)⁠つ')
        self.log.info('KHAI HOA,HELL YEAHHHHH')