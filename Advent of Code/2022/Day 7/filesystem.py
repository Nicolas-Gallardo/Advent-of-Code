from copy import deepcopy

class CommandPrompt:

    def __init__(self, dir):
        self.dir = dir
        self.abs = self.dir

    def cd(self, name):
        try:
            self.dir = self.dir.sub[name]
        except KeyError:
            print("Key error")
        
    def md(self, name):
        self.dir.sub[name] = Directory(name, self.dir)

    def touch(self, name, size):
        self.dir.sub[name] = File(name, size)
        self.abs.update_size()

class Directory:

    def __init__(self, name, parent = None):
        self.name = name
        self.size = 0
        self.sub = {"..":parent} # for subdirectories or files inside in this directory
        self.disk_space = 70000000
        self.space_req_upd = 30000000

    def get_size(self):
        return self.size

    def update_size(self):    
        size = 0
        for i in self.sub:
            if not i == "..":
                if type(self.sub[i]) == Directory:
                    self.sub[i].update_size()
                size += self.sub[i].get_size() 
        self.size = size
        
    def sum_sizes_lte(self, size):
        sum = 0
        if len(self.sub) == 1:
            return 0
        for i in self.sub:
            if not i == ".." and type(self.sub[i]) == Directory:
                if self.sub[i].size <= size:
                    sum += self.sub[i].size
                sum += self.sub[i].sum_sizes_lte(size)
        return sum

    def search_dir_for_update(self, unused_space = 0, dir_sizes = []):
        if unused_space == 0:
            unused_space = self.disk_space - self.size
        if len(self.sub) == 1:
            return
        for i in self.sub:
            if not i == ".." and type(self.sub[i]) == Directory:
                dir_sizes.append(self.sub[i].size)
                self.sub[i].search_dir_for_update(unused_space,dir_sizes)
        dir_sizes.sort()
        for i in dir_sizes:
            if unused_space + i >= self.space_req_upd:
                return i        


    def get_sub(self):
        return deepcopy(self.sub)
    
    def has(self, name, sub = None):
        if sub == None:
            sub = self.get_sub()
        if name in sub:
            return True
        value = False
        for i in sub:
            if not i == ".." and type(sub[i]) == Directory:
                value = value or self.has(name,sub[i].sub)
        return value

    def sub_to_string(self):
        string = ""
        for i in self.sub:
            if not i == "..":
                string += f"{self.sub[i].name} - "
        return string[0:len(string)-3]

    def to_string(self, depth = 1):
        msg = f"- {self.name} (dir, size: {self.size})"
        for i in self.sub:
            if not i == "..":
                if type(self.sub[i]) == Directory:
                    msg += "\n"+"  "*depth+f"{self.sub[i].to_string(depth+1)}"
                else:
                    msg += "\n"+"  "*depth+f"{self.sub[i].to_string()}"
        return msg
    
    def __str__(self):
        return self.to_string()
        
    def __eq__(self, a_dir):
        if self.name == a_dir.name and len(self.sub) == len(a_dir.sub):
            value = True
            for i in self.sub:
                if not i == ".." and i in a_dir.sub:
                    value = value and (self.sub[i] == a_dir.sub[i])
                elif not i == "..":
                    value = False
            return value
        return False

class File:

    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def get_size(self):
        return self.size

    def to_string(self):
        return f"- {self.name} (file, size: {self.size})"

    def __str__(self):
        return self.to_string()
    
    def __eq__(self, a_file):
        if (self.name == a_file.name) and (self.size == a_file.size):
            return True
        else: 
            return False
