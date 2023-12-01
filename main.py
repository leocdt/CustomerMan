import externals
import firebase_admin
import datetime
from firebase_admin import credentials, firestore
from typing import Dict, Any, Union
from typing import Dict, Any, Union
from typing import Dict, Any, Union





def get_client_by_tag(tag: str) -> Union[Dict[str, Any], str]:
    # Retrieve documents from the customer collection
    clients_ref = db.collection('clients')
    query = clients_ref.where('tag', '==', tag)
    docs = query.stream()

    # Retrieve the first document found
    for doc in docs:
        return doc.to_dict()

    return f"Error: No customers have been found for the following tag: {tag}"



def get_client_by_name(name: str) -> Union[Dict[str, Any], str]:
    # Retrieve documents from the customer collection
    clients_ref = db.collection('clients')
    query = clients_ref.where('name', '==', name)
    docs = query.stream()

    # Retrieve the first document found
    for doc in docs:
        return doc.to_dict()

    return f"Error: No customers have been found for the following name: {name}"



def convert_eng_to_eu_date(date: str) -> str:
    # Convert a date from the format YYYY-MM-DD to DD-MM-YYYY
    date_parts = date.split('-')
    date_parts.reverse()
    date = '-'.join(date_parts)
    return date



def get_all_current_clients():
    externals.clear()
    print(externals.green+"Current clients (tag) : \n"+externals.white)

    today = str(datetime.date.today())
    today = convert_eng_to_eu_date(today)

    clients_ref = db.collection('clients')


    # Allows you to retrieve customers whose subscription end date is greater than today's date
    query = clients_ref.where('subscription.end_date', '>=', today)

    docs = query.stream()

    for doc in docs:
        print(doc.to_dict()['tag'])
    


def add_client(name : str, tag : str, start_date : str, end_date : str):
    # Here is an exemple of data to add
    data_to_add = {
        'name': name,
        'tag': tag,
        'subscription': {
            'start_date': start_date,
            'end_date': end_date
        }
    }

    doc_ref = db.collection('clients').add(data_to_add)

    # Retrieve the ID of the added customer
    added_doc_id = doc_ref[1].id

    print(f'Document added with ID: {added_doc_id}')

    return None


def get_clientid_by_name(name : str):
    clients_ref = db.collection('clients')
    query = clients_ref.where('name', '==', name)
    docs = query.stream()

    for doc in docs:
        return doc.id
    


def sup_client_by_tag(tag : str):

    clients_ref = db.collection('clients')
    query = clients_ref.where('tag', '==', tag)
    docs = query.stream()

    for doc in docs:
        doc.reference.delete()
        return f"Ther client {doc.to_dict()['name']} has been deleted"
    
    return f"Error : No customers has been found for the following tag : {tag}"


def update_dates_client(tag : str):
    clients_ref = db.collection('clients')
    query = clients_ref.where('tag', '==', tag)
    docs = query.stream()

    for doc in docs:
        doc.reference.update({
            'subscription.start_date': input("Enter the new start date of the subscription : "),
            'subscription.end_date': input("Enter the new end date of the subscription : ")
        })
        return f"The client {doc.to_dict()['name']} has been updated"
    
    return f"Error : No customers has been found for the following tag : {tag}"
    

def get_client_infos(tag : str):
    clients_ref = db.collection('clients')
    query = clients_ref.where('tag', '==', tag)
    docs = query.stream()

    for doc in docs:
        return doc.to_dict()
    
    return f"Error : No customers has been found for the following tag : {tag}"




def get_client_end_date(tag : str):
    clients_ref = db.collection('clients')
    query = clients_ref.where('tag', '==', tag)
    docs = query.stream()

    for doc in docs:
        return doc.to_dict()['subscription']['end_date']
    
    return f"Error : No customers has been found for the following tag : {tag}"





if __name__ == '__main__':
    cred = credentials.Certificate("YOUR_CONF_FILE.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    res = ""
    while res != '7':
        res = externals.show_mainMenu()
        match res:
            case '1':
                externals.clear()
                get_all_current_clients()
                input("\nPress enter to continue...")
                externals.clear()
            case '2':
                externals.clear()
                name = input("Enter the name of the client : ")
                tag = input("Enter the tag of the client : ")
                start_date = input("Enter the start date of the subscription : ")
                end_date = input("Enter the end date of the subscription : ")
                add_client(name, tag, start_date, end_date)
                input("Press enter to continue...")
                externals.clear()
            case '3':
                externals.clear()
                tag = input("Enter the tag of the client : ")
                update_dates_client(tag)
                input("Press enter to continue...")
                externals.clear()
            case '4':
                externals.clear()
                name = input("Enter the name of the client : ")
                print(get_clientid_by_name(name))
                input("Press enter to continue...")
                externals.clear()
            case '5':
                externals.clear()
                tag = input("Enter the tag of the client : ")
                print(sup_client_by_tag(tag))
                input("Press enter to continue...")
                externals.clear()
            case '6':
                externals.clear()
                tag = input("Enter the tag of the client : ")
                print(get_client_infos(tag))
                input("Press enter to continue...")
                externals.clear()
            case '7':
                externals.clear()
                exit()