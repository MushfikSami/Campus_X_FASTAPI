from app import process_data 

@profile 
def run():
    process_data(1000)

if __name__=='__main__':
    run()