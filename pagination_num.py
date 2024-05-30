class WebScrape:
     def __init__(self, page_range, page):
          self.page_range = page_range
          self.page = page
          
     def pag_rename(self):
          pages = [self.page,]
          for num in self.page_range:
               no = num + 1
               self.page = self.page.replace(str(num), 
               str(no))
               pages.append(self.page)
          return pages
          
     def name(self):
          print(self.page)
          print(self.page_range)
          
          
print("Make sure that the number in the url matches the starting number!!!")
page = str(input("Enter the url:"))
page_range = range(int(input("start: ")), int(input("last:")))

pg1 = WebScrape(page_range, page)
pages = pg1.pag_rename()

#name = pg1.name()

#print(name)
for name in pages:
     print(name)