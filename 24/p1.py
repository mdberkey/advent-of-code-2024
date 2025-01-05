
class Signal:
    def __init__(self, name, val):
        self.name = name
        self.val = val
    
    def __repr__(self):
        return f"<sig: {self.name}, {self.val}>"

def get_outputs(signals, wires, gate_outputs, target_len):
    outputs = []
    seen = set()

    while len(outputs) < target_len:
        for sl in signals:
            do_break = False
            for sr in signals:
                if sr.name in wires[sl.name]["AND"]:
                    if (sl, sr, "AND") in seen or (sr, sl, "AND") in seen:
                        continue
                    out_val = sl.val & sr.val
                    seen.add((sl, sr, "AND"))
                    seen.add((sr, sl, "AND"))
                elif sr.name in wires[sl.name]["OR"]:
                    if (sl, sr, "OR") in seen or (sr, sl, "OR") in seen:
                        continue
                    out_val = sl.val | sr.val
                    seen.add((sl, sr, "OR"))
                    seen.add((sr, sl, "OR"))
                elif sr.name in wires[sl.name]["XOR"]:
                    if (sl, sr, "XOR") in seen or (sr, sl, "XOR") in seen:
                        continue
                    out_val = sl.val ^ sr.val
                    seen.add((sl, sr, "XOR"))
                    seen.add((sr, sl, "XOR"))
                else:
                    continue

                out_name = gate_outputs[(sl.name, sr.name)]

                if out_name.startswith("z"):
                    outputs.append(Signal(out_name, out_val))
                else:
                    signals.append(Signal(out_name, out_val))
                do_break = True
                break

            if do_break:
                break
    
    return outputs

if __name__ == "__main__":
    sec1, sec2 = open("24/i00.txt").read().split("\n\n")
    wires = {}
    signals = []
    gate_outputs = {}

    for line in sec1.splitlines():
        name, val = line.split(": ")
        wires[name] = {"AND": [], "OR": [], "XOR": []}
        signals.append(Signal(name, int(val)))

    for line in sec2.splitlines():
        l, out = line.split(" -> ")
        opl, op, opr = l.split() 
        if opl not in wires:
            wires[opl] = {"AND": [], "OR": [], "XOR": []}
        if opr not in wires:
            wires[opr] = {"AND": [], "OR": [], "XOR": []}
        wires[opl][op].append(opr)
        wires[opr][op].append(opl)
        gate_outputs[(opl, opr)] = out
        gate_outputs[(opr, opl)] = out
    
    z_outs = set() 
    for out in gate_outputs.values():
        if out.startswith("z"):
            z_outs.add(out)
    
    outputs = get_outputs(signals, wires, gate_outputs, len(z_outs))
    b_string = "".join([str(sig.val) for sig in outputs][::-1])

    print(int(b_string, 2))