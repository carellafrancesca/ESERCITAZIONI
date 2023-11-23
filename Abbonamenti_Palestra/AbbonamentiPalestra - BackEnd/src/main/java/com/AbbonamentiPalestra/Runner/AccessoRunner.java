package com.AbbonamentiPalestra.Runner;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import com.AbbonamentiPalestra.Service.UtenteAccessoService;

@Component
public class AccessoRunner implements CommandLineRunner{

	@Autowired UtenteAccessoService usersvc;
	
	@Override
	public void run(String... args) throws Exception {
		System.out.println("Accesso Login Runner...");
	
		//usersvc.createTestUser("francesca", "password");
		
	}

}
