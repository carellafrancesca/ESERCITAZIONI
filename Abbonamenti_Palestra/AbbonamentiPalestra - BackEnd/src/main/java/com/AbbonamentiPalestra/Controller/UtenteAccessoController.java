package com.AbbonamentiPalestra.Controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.AbbonamentiPalestra.Service.UtenteAccessoService;
import com.AbbonamentiPalestraDTO.LoginRequest;

@RestController
@CrossOrigin(origins = "*")
@RequestMapping("/api/login")
public class UtenteAccessoController {

    @Autowired UtenteAccessoService utenteAccessoService;
	
    @PostMapping
    public String login(@RequestBody LoginRequest loginRequest) {
    	
        String username = loginRequest.getUsername();
        String password = loginRequest.getPassword();
    	
        if(utenteAccessoService.login(username, password)) {
        	return "Login riuscito!";
        } else {
        	return "Credenziali non valide";
        }
        
    }
}
