import click
import sqlite3



@click.command()
@click.option('--add_item',
            default='',      
            prompt='Add Item To List: ', 
            help='Item you want to add to the TODO list.')
@click.option('--remove_item', 
            default='',
            prompt='Remove Item From List: ', 
            help='Item you want to remove from the TODO list.')
@click.option('--show_items', 
            default='',
            prompt='Show Items Within The List: ', 
            help='All items currently in the TODO list.')

def hello(add_item, remove_item, show_items):
    """Program that stores items in a TODO list.  use the --help command for help
    with commands!"""
    if add_item is not '':
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO list VALUES (?)", (add_item, ))
        conn.commit()
        conn.close()

    # if remove_item is not '':
    #     conn = sqlite3.connect('database.db')
    #     c = conn.cursor()
    #     c.execute("DELETE FROM tasks WHERE id=?", remove_item)
    #     conn.close()

    if show_items is not '':
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM list")
        rows = c.fetchall()

        for row in rows:
            print(row)
        
        conn.close()

        
if __name__ == '__main__':
    hello()
