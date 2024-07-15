import pickle

class PersistenceUtils:

    @staticmethod
    def write_pickle(file_name,data):
        #pickle_file = os.path.join('./', 'customer_data.pickle')
        with open(file_name,'wb') as file:
            pickle.dump(data,file)
        pass

    @staticmethod
    def load_pickle(file_path):
        with open(file_path,'rb') as file:
            data = pickle.load(file)
        return data


