import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/Top-Rated/api/e-mail-check-invalid-or-disposable-domain'

mcp = FastMCP('e-mail-check-invalid-or-disposable-domain')

@mcp.tool()
def mailcheck(domain: Annotated[str, Field(description='Full e-mail, or domain to check if valid or temporary/disposable. You can enter an e-mail address, and it will be converted to a domain, but entering just the domain is recommended for user privacy reasons.')]) -> dict: 
    '''Check if e-mail domain is valid, or a disposable/temporary address. Invalid domains (typos, non-responding mailserver, etc) will return "valid: false", "block: true". Disposable e-mail domains will return "valid: true" (since it's a valid domain), but "block: true" and "disposable: true".'''
    url = 'https://mailcheck.p.rapidapi.com/'
    headers = {'x-rapidapi-host': 'mailcheck.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'domain': domain,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
