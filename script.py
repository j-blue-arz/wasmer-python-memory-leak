from cmd import Cmd
import gc
import os

import psutil
from wasmer import engine, wasi, Store, Module, Instance
from wasmer_compiler_cranelift import Compiler


class Prompt(Cmd):
    def __init__(self):
        self._process = psutil.Process(os.getpid())
        super().__init__()

    def do_run(self, inp):
        with open("hello.wasm", "rb") as f:
            wasm_bytes = f.read()
        store = Store(engine.Universal(Compiler))
        module = Module(store, wasm_bytes)
        wasi_version = wasi.get_version(module, strict=True)
        wasi_env = wasi.StateBuilder("foo").finalize()
        import_object = wasi_env.generate_import_object(store, wasi_version)
        instance = Instance(module, import_object)
        instance.exports.hello()

    def do_gc(self, inp):
        gc.collect()

    def do_rss(self, inp):
        print(f"rss: {self._process.memory_info().rss / 1024 ** 2:.2f} MiB")

    def do_exit(self, inp):
        """exit the application."""
        print("Bye")
        return True


Prompt().cmdloop()
