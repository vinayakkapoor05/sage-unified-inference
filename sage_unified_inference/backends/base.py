from typing import Protocol, Dict, Any 

class Backend(Protocol):
    name: str 
    async def infer(self, payload: Dict[str, Any] -> Dict[str, Any]):
        pass 

    
