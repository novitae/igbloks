from . import tree

class Layout:
    def __init__(
        self,
        tree: dict | tree.Branch
    ) -> None:
        if isinstance(tree, dict):
            

    @classmethod
    def from_dict(
        cls,
        d: dict
    ) -> "Layout":
        if recursed := d.pop("layout", None):
            d = recursed
        if recursed := d.pop("bloks_payload", None):
            d = recursed
        elif not all([key in d for key in ["tree", "data", "error_attribution"]]):
            raise ValueError( 'Impossible to find the appropriate keys to init'
                              ' properly the `Layout` class.' )
        else:
            return cls(**d)