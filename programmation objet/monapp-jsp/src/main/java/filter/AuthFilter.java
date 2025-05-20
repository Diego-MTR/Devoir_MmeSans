package filter;

import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.*;
import java.io.IOException;

@WebFilter("/*")
public class AuthFilter implements Filter {
    public void doFilter(ServletRequest req, ServletResponse resp, FilterChain chain)
            throws IOException, ServletException {
        HttpServletRequest request = (HttpServletRequest) req;
        HttpServletResponse response = (HttpServletResponse) resp;
        String uri = request.getRequestURI();

        boolean loggedIn = (request.getSession().getAttribute("user") != null);
        boolean loginRequest = uri.endsWith("login") || uri.endsWith("login.jsp") || uri.endsWith(".css");

        if (loggedIn || loginRequest) {
            chain.doFilter(req, resp);
        } else {
            response.sendRedirect("login");
        }
    }
}