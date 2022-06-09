import os 
if __name__ == "__main__":
        try:
                __import__("revax").tampilan_menu()
        except Exception as e:
                exit(str(e))
