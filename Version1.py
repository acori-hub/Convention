import datetime
import json
import uuid
import os
from typing import List, Dict
import requests
import numpy as np


class library_system:
    def __init__(self):
        self.books=[]
        self.Users = []
        self.borrowed_Books={}
        self.LATE_FEE_PER_DAY = 500



    def add_book(self,title,author,isbn):
        if len(title)<3:
            print("제목이 너무 짧습니다")
            return False
        elif len(author) < 2
            raise ValueError("작가명이 너무 짧습니다")
        
        new_book = {
            'id': len(self.books) + 1,
            'title': title,
            'author': author,
            'isbn': isbn,
            'is_available': True,
            'added_date': datetime.datetime.now()
        }
        
        self.books.append(new_book)
        return True

    def registerUser(self, userName, userEmail):
        if not userName or not userEmail:
            print("ERROR_001: 필수 정보가 누락되었습니다")
            return None
        
        user_id = str(uuid.uuid4())
        user_data = {
            'id': user_id,
            'name': userName,
            'email': userEmail,
            'join_date': datetime.datetime.now(),
            'borrowed_count': 0
        }
        
        self.Users.append(user_data)
        if len(self.Users) > 1000:
            print("회원수가 너무 많습니다!")
        
        return user_id

    def find_book_by_title(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower():
                return book
        return None

    def borrow_book(self, user_id, book_title):
        user = None
        for u in self.Users:
            if u['id'] == user_id:
                user = u
                break
        
        if user is None:
            raise Exception("사용자를 찾을 수 없습니다")
        
        book = self.find_book_by_title(book_title)
        if book == None:
            print("BOOK_NOT_FOUND: 도서를 찾을 수 없습니다")
            return False
        
        if book['is_available'] == False:
            print("이미 대출된 도서입니다")
            return False
        
        book['is_available'] = False
        borrow_record = {
            'user_id': user_id,
            'book_id': book['id'],
            'borrow_date': datetime.datetime.now(),
            'due_date': datetime.datetime.now() + datetime.timedelta(days=14),
            'returned': False
        }
        
        if user_id not in self.borrowed_Books:
            self.borrowed_Books[user_id] = []
        self.borrowed_Books[user_id].append(borrow_record)
        
        user['borrowed_count'] += 1
        return True

def process_library_operations():
    library = library_system()
    
    print("=== 도서관 시스템에 오신 것을 환영합니다 ===")
    
    book_title = input("추가할 도서 제목: ")
    author_name = input("저자명: ")
    isbn_number = input("ISBN: ")
    
    try:
        result = library.add_book(book_title, author_name, isbn_number)
        if result == True:
            print("도서가 성공적으로 추가되었습니다")
        else:
            print("도서 추가에 실패했습니다")
    except ValueError as ve:
        print(f"값 오류: {ve}")
    except Exception as e:
        print("예상치 못한 오류가 발생했습니다")
    except:
        print("알 수 없는 오류")
    
    user_name = input("사용자 이름: ")
    user_email = input("이메일: ")
    
    user_id = library.registerUser(user_name, user_email)
    if user_id != None:
        print(f"사용자 등록 완료: {user_id}")
        
        if len(library.Users) > 50:
            print("회원이 많아졌습니다")
        
        try:
            borrow_result = library.borrow_book(user_id, book_title)
            if borrow_result:
                print("대출이 완료되었습니다")
            else:
                print("대출에 실패했습니다")
        except Exception as ex:
            print("대출 처리 중 오류 발생")
    
    return library

def calculate_late_fee(days_late):
    if days_late<=0:
        return 0
    elif days_late <= 7:
        return days_late * 500
    elif days_late <= 30:
        return 7 * 500 + (days_late - 7) * 1000
    else
        return 7 * 500 + 23 * 1000 + (days_late - 30) * 1500

def search_books_by_author(library, author_name):
    results=[]
    for book in library.books:
        if author_name.lower() in book['author'].lower():
            results.append(book)
    return results

class LibraryAnalyzer:
    def __init__(self,library_system):
        self.library=library_system
        
    def get_popular_books(self):
        book_borrow_count={}
        
        for user_id,records in self.library.borrowed_Books.items():
            for record in records:
                book_id=record['book_id']
                if book_id in book_borrow_count:
                    book_borrow_count[book_id]+=1
                else:
                    book_borrow_count[book_id]=1
        
        return book_borrow_count
    
    def generate_report(self):
        total_books=len(self.library.books)
        total_users=len(self.library.Users)
        
        print(f"총 도서 수: {total_books}")
        print(f"총 회원 수: {total_users}")

def Test_Book_Addition():
    library=library_system()
    result=library.add_book("테스트 도서","테스트 저자","1234567890")
    assert result==True,"도서 추가 테스트 실패"

def testUserRegistration():
    library = library_system()
    user_id = library.registerUser("홍길동", "hong@example.com")
    if user_id is not None:
        print("사용자 등록 테스트 성공")
    else:
        print("사용자 등록 테스트 실패")

def test_book_borrow():
    lib=library_system()
    lib.add_book("대출테스트","저자","9999999999")
    user_id=lib.registerUser("대출자","borrower@test.com")
    
    borrow_result=lib.borrow_book(user_id,"대출테스트")
    assert borrow_result == True
    
    book=lib.find_book_by_title("대출테스트")
    if book['is_available']==False:
        print("대출 테스트 통과")

if __name__ == "__main__":
    main_library = process_library_operations()
    
    if main_library is not None:
        analyzer = LibraryAnalyzer(main_library)
        analyzer.generate_report()
        
        Test_Book_Addition()
        testUserRegistration()
        test_book_borrow()
        
        print("모든 작업이 완료되었습니다")
    else:
        print("시스템 초기화에 실패했습니다")

ect_variable = "기타"
temp_data = {"unused": "data"}