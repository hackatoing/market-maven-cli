import click
import sqlite3


@click.group()
def cli():
    pass


@click.command()
def initdb():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE stocks(id, ticker, quantity, price, operation_date, operation)")


@click.command()
@click.option('--ticker', help='Stock ticker', required=True, type=str)
@click.option('--quantity', help='Quantity of stocks', required=True, type=int)
@click.option('--price', help='Price of a stock', required=True, type=float)
@click.option('--operation-date', help='Date of acquisition', required=True, type=click.DateTime(formats=["%Y-%m-%d"]))
@click.option('--operation',
              help='Operation type (buy or sell)',
              required=True,
              type=click.Choice(['BUY', 'SELL'], case_sensitive=False))
def add_stock(ticker, quantity, price, operation_date, operation):
    click.echo(f"Ticker: {ticker}, Quantity: {quantity}, Price: {price}, Operation date: {operation_date}, Operation: {operation}")


if __name__ == '__main__':
    cli.add_command(initdb)
    cli.add_command(add_stock)
    cli()
