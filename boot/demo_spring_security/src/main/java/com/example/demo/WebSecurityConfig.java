package com.example.demo;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.crypto.factory.PasswordEncoderFactories;
import org.springframework.security.crypto.password.PasswordEncoder;

@Configuration
@EnableWebSecurity // 이걸 쓰는 순간 기본 security 설정은 날아감
public class WebSecurityConfig extends WebSecurityConfigurerAdapter  {

	@Override
	protected void configure(HttpSecurity http) throws Exception {
		http.authorizeRequests()
				.antMatchers("/", "/home","/create").permitAll() // 이 path로 접근하지 않았을때 SecurityContext에 Authentication 객체가 등록되있지 않으면 formLogin으로 보낸다.
				//.antMatchers("/admin/**").hasRole("ADMIN")
				.anyRequest().authenticated()
				.and()
			.formLogin()
				.loginPage("/login")
				.permitAll()
				.and()
			.logout()
				.logoutSuccessUrl("/home")
				.permitAll();
	}
	
	
	
	/*@Bean
	@Override
	protected UserDetailsService userDetailsService() {
		UserDetails user =
				User.withDefaultPasswordEncoder()
					.username("user")
					.password("password")
					.roles("USER")
					.build();
		
		return new InMemoryUserDetailsManager(user);
	}*/
	
	
	@Bean
	public PasswordEncoder passwordEncoder() {
		return PasswordEncoderFactories.createDelegatingPasswordEncoder();
	}
}
