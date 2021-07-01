#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/args.hpp>

using namespace boost::python;

double aaa(int x, int y)
{
    return 0.1;
}

BOOST_PYTHON_MODULE(numpypp)
{
    def("aaa", aaa, args("x", "y"), "foo's docstring");
}
