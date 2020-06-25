#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/args.hpp>

using namespace boost::python;

int foo(int x, int y) { return x * y; }

BOOST_PYTHON_MODULE(func_args)
{
    def("foo", foo, args("x", "y"), "foo's docstring");
}

