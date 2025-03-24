from abc import ABC
from dataclasses import dataclass


class Exp(ABC):
    def eval(self):
        pass

    def printPrefix(self):
        pass


@dataclass
class BinExp(Exp):
    left: Exp
    op: str
    right: Exp

    def eval(self):
        left_val = self.left.eval()
        right_val = self.right.eval()

        if self.op == "+":
            return left_val + right_val
        elif self.op == "-":
            return left_val - right_val
        elif self.op == "*":
            return left_val * right_val
        else:
            return left_val / right_val

    def printPrefix(self):
        return f"{self.op} {self.left.printPrefix()} {self.right.printPrefix()}"


@dataclass
class UnExp(Exp):
    op: str
    operand: Exp

    def eval(self):
        operand_val = self.operand.eval()
        if self.op == "+":
            return +operand_val
        else:
            return -operand_val

    def printPrefix(self):
        return f"{self.op}. {self.operand.printPrefix()}"


@dataclass
class IntLit(Exp):
    val: int

    def eval(self):
        return self.val

    def printPrefix(self):
        return self.val


@dataclass
class FloatLit(Exp):
    val: float

    def eval(self):
        return self.val

    def printPrefix(self):
        return self.val
